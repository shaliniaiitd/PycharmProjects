import os
import sys
import json
import pathlib
import configparser
import logging
from typing import TextIO, List, Any

from constants import Constant as constant

# logging
logger = logging.getLogger(__name__)
logger.setLevel(constant.LOG_LEVEL)

# console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(constant.LOG_LEVEL)
console_handler.setFormatter(logging.Formatter(constant.FRMT_STR, constant.DATE_STR))

# file handler
file_handler = logging.FileHandler(constant.LOG_FILE_NAME)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(constant.FRMT_STR, constant.DATE_STR))

logger.addHandler(console_handler)
logger.addHandler(file_handler)


class PyModule:
    """
    Its a data class to represent a python module
    """

    def __init__(self, module_name):
        self.module_name = module_name
        self.import_statements = ""
        self.class_initialization = ""
        self.class_var_initializations = []
        self.class_constructor = ""
        self.class_methods = []

    def get_module_content(self):
        module_content = self.class_initialization + \
                         "".join(self.class_var_initializations) + \
                         self.class_constructor + \
                         "".join(self.class_methods)
        return module_content


class PyModuleBuilder:
    """
    Its Python module builder helper class.
    """

    def __init__(self):
        self.py_modules = {}

    def create_new_module(self, module_name):
        if module_name not in self.py_modules:
            self.py_modules[module_name] = PyModule(module_name)

    def add_class_initialization_content(self, module_name, content):
        if module_name in self.py_modules:
            self.py_modules[module_name].class_initialization = content
        else:
            logger.error("invalid module name")

    def add_class_var_initialization_content(self, module_name, content_vars):
        if module_name in self.py_modules:
            for var in content_vars:
                self.py_modules[module_name].class_var_initializations.append(var)
        else:
            logger.error("invalid module name")

    def add_class_constructor_content(self, module_name, content_constructor):
        if module_name in self.py_modules:
            self.py_modules[module_name].class_constructor = content_constructor
        else:
            logger.error("invalid module name")

    def add_class_methods_content(self, module_name, content_methods):
        if module_name in self.py_modules:
            for method in content_methods:
                self.py_modules[module_name].class_methods.append(method)
        else:
            logger.error("invalid module name")


class POMJsonParser:
    """
    It's a class to parse and validate POM Json
    """

    def __init__(self, pom_data):
        self.pom_data = pom_data

    def get_page_name(self):
        return self.pom_data[constant.PAGE_NAME]

    def get_operation(self):
        return self.pom_data[constant.OPERATION]

    def get_parent_class_name(self):
        if self.pom_data[constant.PARENT_CLASS_NAME].upper() == constant.NOT_APPLICABLE:
            return constant.BASE_CLASS_NAME
        return self.pom_data[constant.PARENT_CLASS_NAME]

    def get_child_class_names(self):
        return self.pom_data[constant.CHILD_CLASS_NAMES]

    def get_locators(self):
        return self.pom_data[constant.LOCATERS]

    def get_element_name_of_locator(self, locator_json):
        return locator_json[constant.ELEMENT_NAME]

    def get_element_type_of_locator(self, locator_json):
        return locator_json[constant.ELEMENT_TYPE]

    def get_element_locator_identifier_type_of_locator(self, locator_json):
        return locator_json[constant.LOCATOR_IDENTIFIER_TYPE]

    def get_element_locator_identifier_value_of_locator(self, locator_json):
        return locator_json[constant.LOCATOR_IDENTIFIER_VALUE]

    def get_element_action_methods_of_locator(self, locator_json):
        return locator_json[constant.ELEMENT_ACTION_METHODS].split(",")

    def get_element_verification_methods_of_locator(self, locator_json):
        return locator_json[constant.ELEMENT_VERFICATION_METHODS].split(",")

    def validate_json_and_get_errors(self):
        errors = []

        # validating keys
        for key in constant.JSON_POM_KEYS:
            if key not in self.pom_data:
                msg = "{} is not present as key in Pom Data".format(key)
                errors.append(msg)

        # validating locators
        for index, locator in enumerate(self.get_locators()):
            for key in constant.JSON_LOCATOR_KEYS:

                # Validating locator keys
                if key not in locator:
                    msg = "{} is not present as key in {} Locator in Pom Data".format(key, index + 1)
                    errors.append(msg)

            # Validating element type
            if locator[constant.ELEMENT_TYPE] not in constant.WEB_ELEMENT_TYPES:
                msg = "Element type {} of {} locator is not present in supported Element types".format(
                    locator[constant.ELEMENT_TYPE], index)
                errors.append(msg)

            # Validating identifier type
            if locator[constant.LOCATOR_IDENTIFIER_TYPE] not in constant.JSON_LOCATOR_IDENTIFIER_TYPES:
                msg = "Element Locator Identifier type {} of {} locator is not present in supported Identifier type".format(
                    locator[constant.LOCATOR_IDENTIFIER_TYPE], index)
                errors.append(msg)

            # Validating action methods
            for method in locator[constant.ELEMENT_ACTION_METHODS].split(","):
                if method != "":
                    if method not in constant.WEB_ELE[locator[constant.ELEMENT_TYPE]].split(","):
                        msg = "Action method {} of element type {} of {} locator is not present in supported action method".format(
                            method, locator[constant.ELEMENT_TYPE], index)
                        errors.append(msg)

            # Validating verification methods
            for method in locator[constant.ELEMENT_VERFICATION_METHODS].split(","):
                if method != "":
                    if method not in constant.WEB_ELE_VER_MAP[locator[constant.ELEMENT_TYPE]].split(","):
                        msg = "Verification method {} of element type {} of {} locator is not present in supported verification method".format(
                            method, locator[constant.ELEMENT_TYPE], index)
                        errors.append(msg)

        return len(errors) == 0, errors


class POMGenerator:

    def __init__(self):
        # initializing
        self.config = None
        self.input_dir_path = None
        self.root_dir = None
        self.output_dir_path = None
        self.project_folder_name = None
        self.pom_dir_name = None
        self.json_files = None
        self.poms_data = []
        self.json_parser_objs = []

        self.setup()

    def setup(self):
        # reading config file
        self.config = configparser.RawConfigParser()
        self.config.read(constant.CONFIG_FILE_PATH)
        # reading input and output directory path from config
        try:
            # input_path = self.config.get('common info', 'json_dir_path')
            input_path = os.getcwd()+'\\pagejsons'

            if input_path.upper() == constant.NOT_APPLICABLE:
                self.input_dir_path = os.getcwd()
            else:
                self.input_dir_path = input_path
        except configparser.NoOptionError:
            logger.error("source directory configuration error in config.cfg")

        try:
            # self.root_dir = self.config.get('common info', 'root_dir')
            self.root_dir = os.path.abspath('../')
            self.project_folder_name = self.config.get('common info', 'project_folder_name')
            self.pom_dir_name = self.config.get('common info', 'pom_dir_name')
            if self.root_dir.upper() == constant.NOT_APPLICABLE:
                self.root_dir = os.getcwd()
            if self.project_folder_name.upper() == constant.NOT_APPLICABLE:
                self.project_folder_name = constant.DEFAULT_PROJECT_DIR
            if self.pom_dir_name.upper() == constant.NOT_APPLICABLE:
                self.pom_dir_name = constant.DEFAULT_POM_DIR
            self.output_dir_path = os.path.join(self.root_dir, self.project_folder_name, self.pom_dir_name)
        except configparser.NoOptionError:
            logger.error("destination directory configuration error in config.cfg")

    def execute(self, operation):
        if operation == "validate" or operation == "v":
            self.process_all_poms()
        elif operation == "write" or operation == "w":
            self.process_all_poms(True)
        else:
            logger.error("Invalid Operation flow")

    def process_all_poms(self, write=False):
        # getting list of json files
        self.json_files = self.get_list_of_json_files()

        # getting json data dump for all files
        for file in self.json_files:
            self.poms_data.append(self.get_json_data_dump(file))

        # creating POMJson Parser object for each pom data and processing it.
        py_builder_obj = PyModuleBuilder()
        count = 0
        for pom in self.poms_data:
            pom_json_obj = POMJsonParser(pom[0])
            if self.validate_pom(pom_json_obj) and write:
                self.process_a_pom(pom_json_obj, py_builder_obj, write)
            count += 1
        msg = "--- Processing completed for {} pom object(s) for Actions and Verification classes. --- ".format(count)
        logger.info(msg)

    def validate_pom(self, pom_json_obj):
        er_not_found, errors = pom_json_obj.validate_json_and_get_errors()
        if er_not_found:
            logger.info(
                "-------------------- No Error occurred, Successfully validated POM : {} -----------------------".format(
                    pom_json_obj.get_page_name()))
            return True
        else:
            logger.info(
                "-------------------- Error occurred for POM: {} -----------------------".format(
                    pom_json_obj.get_page_name()))
            for error in errors:
                logger.error(error)
            return False

    def process_a_pom(self, pom_json_obj, py_builder_obj, write=False, print_pom=False):
        # getting class names
        action_class_name = pom_json_obj.get_page_name()
        verification_class_name = action_class_name + constant.BASE_CLASS_NAME_POSTFIX_TEXT

        # ## --  creating action module schema -- ##
        py_builder_obj.create_new_module(action_class_name)
        # class initialization
        py_builder_obj = self.process_import_and_class_initialization(pom_json_obj, py_builder_obj, action_class_name)

        # class Variable initialization
        py_builder_obj = self.process_class_vars(pom_json_obj, py_builder_obj)

        # class constructor
        py_builder_obj = self.process_class_constructor(pom_json_obj, py_builder_obj, action_class_name)

        # class methods
        py_builder_obj = self.process_class_action_methods(pom_json_obj, py_builder_obj)

        # ## --  creating Verification module schema -- ##
        py_builder_obj.create_new_module(verification_class_name)
        # class initialization
        py_builder_obj = self.process_import_and_class_initialization(pom_json_obj, py_builder_obj,
                                                                      verification_class_name, "verification")

        # class constructor
        py_builder_obj = self.process_class_constructor(pom_json_obj, py_builder_obj, verification_class_name,
                                                        "verification")

        # class methods
        py_builder_obj = self.process_class_verification_methods(pom_json_obj, py_builder_obj, verification_class_name)

        # Saving POM file
        if write:
            self.py_pom_writer(action_class_name, os.path.join(self.output_dir_path, constant.ACTION_POM_DIR_NAME),
                               py_builder_obj)
            self.py_pom_writer(verification_class_name,
                               os.path.join(self.output_dir_path, constant.VERIFICATION_POM_DIR_NAME),
                               py_builder_obj)

        # Printing POM data
        if print_pom:
            self.print_pom(action_class_name, py_builder_obj)
            self.print_pom(verification_class_name, py_builder_obj)

    def process_import_and_class_initialization(self, pom_obj, py_builder_obj, class_name, type_of_class="action"):

        if type_of_class == "action":
            parent_class_name = pom_obj.get_parent_class_name()
            class_initialization_content = constant.BASE_CLASS_PATH + constant.DOUBLE_NEW_LINE
        else:
            parent_class_name = pom_obj.get_page_name()
            class_initialization_content = constant.BASE_CLASS_PATH_FOR_VERIFICATION.substitute(
                project_folder_name=self.project_folder_name,
                pom_dir_name=self.pom_dir_name,
                page_name=parent_class_name) + constant.DOUBLE_NEW_LINE

        class_initialization_content += constant.CLASS_INITIALIZATION_STATEMENT.substitute(class_name=class_name,
                                                                                           parent_class_name=parent_class_name) + constant.SINGLE_NEW_LINE
        py_builder_obj.add_class_initialization_content(class_name, class_initialization_content)
        return py_builder_obj

    def process_class_vars(self, pom_obj, py_builder_obj):
        class_name = pom_obj.get_page_name()
        locators = pom_obj.get_locators()

        class_variable_initialization_content = ""
        for item in locators:
            locator_value = item[constant.LOCATOR_IDENTIFIER_VALUE]
            locator_name_post_fix = ""
            if constant.DYNAMIC_VAR_REPLACER in locator_value:
                locator_value = locator_value.replace(constant.DYNAMIC_VAR_REPLACER, "{}")
                locator_name_post_fix = constant.DYNAMIC_VAR_POSTFIX
            variable_n = constant.WEB_ELEMENT_TYPES[item[constant.ELEMENT_TYPE]] + "_" + item[
                constant.ELEMENT_NAME] + locator_name_post_fix
            variable_v = item[constant.LOCATOR_IDENTIFIER_TYPE] + constant.LOCATOR_TYPE_VALUE_SEPARATOR + locator_value
            class_variable_initialization_content += constant.SINGLE_TAB + \
                                                     constant.CLASS_VARIABLE_INITIALIZATION_STATEMENT.substitute(
                                                         variable_name=variable_n,
                                                         variable_value=variable_v) + \
                                                     constant.SINGLE_NEW_LINE

        class_variable_initialization_content += constant.SINGLE_NEW_LINE

        py_builder_obj.add_class_var_initialization_content(class_name, class_variable_initialization_content)
        return py_builder_obj

    def process_class_constructor(self, pom_obj, py_builder_obj, class_name, type_of_class="action"):

        class_constructor_content = constant.CLASS_CONSTRUCTOR_METHOD_INITIALIZATION \
                                    + constant.SINGLE_NEW_LINE \
                                    + constant.CLASS_CONSTRUCTOR_METHOD_SUPER_STATEMENT.substitute(
            class_name=class_name) \
                                    + constant.DOUBLE_NEW_LINE

        py_builder_obj.add_class_constructor_content(class_name, class_constructor_content)
        return py_builder_obj

    def process_class_action_methods(self, pom_obj, py_builder_obj):
        class_name = pom_obj.get_page_name()

        for locator in pom_obj.get_locators():
            for action_method in pom_obj.get_element_action_methods_of_locator(locator):
                if action_method !="":
                    method_name_parameters = constant.ACTION_MAP[action_method].split(",")
                    method_name = method_name_parameters[0]
                    parameters = ""
                    if len(method_name_parameters) > 1:
                        parameters = ", ".join(method_name_parameters[1:])
                        parameters = ", " + parameters
                    element_name = constant.WEB_ELEMENT_TYPES[locator[constant.ELEMENT_TYPE]] + "_" + locator[
                        constant.ELEMENT_NAME]
                    dynamic_param = ""
                    dynamic_format = ""
                    if constant.DYNAMIC_VAR_REPLACER in locator[constant.LOCATOR_IDENTIFIER_VALUE]:
                        dynamic_param = constant.DYNAMIC_NTH_PARAMETER
                        dynamic_format = constant.DYNAMIC_VAR_FORMAT
                        element_name += constant.DYNAMIC_VAR_POSTFIX
                    method_content = constant.CLASS_METHOD_INITIALIZATION.substitute(method_name=method_name,
                                                                                     element_name=element_name,
                                                                                     parameters=parameters + dynamic_param) + constant.SINGLE_NEW_LINE
                    method_content += constant.COMM_STR.substitute(action=action_method, element_name=element_name)
                    method_return_type = constant.METHOD_RETURN_MAP[action_method]
                    if "return" in method_return_type:
                        method_content += constant.CLASS_METHOD_CALL_STATEMENT.substitute(return_option="return ",
                                                                                          associated_obj="do",
                                                                                          method_name=method_name,
                                                                                          element_name=element_name + dynamic_format,
                                                                                          parameters=parameters) + constant.SINGLE_NEW_LINE
                    elif "self" in method_return_type:
                        method_content += constant.CLASS_METHOD_CALL_STATEMENT.substitute(return_option="",
                                                                                          associated_obj="do",
                                                                                          method_name=method_name,
                                                                                          element_name=element_name + dynamic_format,
                                                                                          parameters=parameters) + constant.SINGLE_NEW_LINE
                        method_content += constant.CLASS_METHOD_RETURN_STATEMENT.substitute(
                            return_obj="self") + constant.SINGLE_NEW_LINE
                    elif "blank" in method_return_type:
                        method_content += constant.CLASS_METHOD_CALL_STATEMENT_NO_PARAM.substitute(return_option="",
                                                                                          associated_obj="do",
                                                                                          method_name=method_name) + constant.SINGLE_NEW_LINE
                        method_content += constant.CLASS_METHOD_RETURN_STATEMENT.substitute(
                            return_obj="self") + constant.SINGLE_NEW_LINE
                    method_content += constant.SINGLE_NEW_LINE
                    py_builder_obj.add_class_methods_content(class_name, method_content)
        return py_builder_obj

    def process_class_verification_methods(self, pom_obj, py_builder_obj, class_name):

        for locator in pom_obj.get_locators():
            for verification_method in pom_obj.get_element_verification_methods_of_locator(locator):
                if verification_method !="":
                    method_name_parameters = constant.VER_METHOD_MAP[verification_method].split(",")
                    method_name = method_name_parameters[0]
                    parameters = ""
                    if len(method_name_parameters) > 1:
                        parameters = ", ".join(method_name_parameters[1:])
                        parameters = ", " + parameters
                    element_name = constant.WEB_ELEMENT_TYPES[locator[constant.ELEMENT_TYPE]] + "_" + locator[
                        constant.ELEMENT_NAME]
                    if constant.DYNAMIC_VAR_REPLACER in locator[constant.LOCATOR_IDENTIFIER_VALUE]:
                        parameters += constant.DYNAMIC_NTH_PARAMETER
                        element_name += constant.DYNAMIC_VAR_POSTFIX
                    method_content = constant.CLASS_METHOD_INITIALIZATION.substitute(method_name=method_name,
                                                                                     element_name=element_name,
                                                                                     parameters=parameters) + constant.SINGLE_NEW_LINE
                    method_content += constant.COMM_STR.substitute(action=verification_method, element_name=element_name)
                    method_content += constant.CLASS_METHOD_CALL_STATEMENT.substitute(return_option="return ",
                                                                                      associated_obj="verify",
                                                                                      method_name=method_name,
                                                                                      element_name=element_name,
                                                                                      parameters=parameters) + constant.SINGLE_NEW_LINE
                    method_content += constant.SINGLE_NEW_LINE
                    py_builder_obj.add_class_methods_content(class_name, method_content)
        return py_builder_obj

    def get_list_of_json_files(self) -> List[str]:
        """
        it Reads the list of Json files in the current folder or provided path and returns a list with file names
        Input : None
        """
        files: List[str] = []

        try:
            for file in os.listdir(self.input_dir_path):
                if file.endswith('.json'):
                    json_file: TextIO = open(os.path.join(self.input_dir_path, file))
                    files.append(json_file.name)
            return files
        except FileNotFoundError as fileNotFoundError:
            logger.error(fileNotFoundError)
        if len(files) != constant.SIZE_ZERO:
            return files
        else:
            msg = "JSON Files are not presented in the tool directory to parse"
            logger.error(msg)
            raise Exception(msg)

    def get_json_data_dump(self, json_file_path) -> None:
        with open(json_file_path, 'r') as json_input_file:
            msg = ('######## ' + json_input_file.name + " Reading Json Files Data " + '########')
            logger.info(msg)
            dump: Any = json.load(json_input_file)
            return dump

    def py_pom_writer(self, file_name: str, file_dir_path: str, py_builder_obj: PyModuleBuilder) -> None:
        file_to_save = os.path.join(file_dir_path, file_name + ".py")

        try:
            pathlib.Path(file_dir_path).mkdir(parents=True, exist_ok=True)
            with open(file_to_save, "w") as fl_to_wr:
                for value in py_builder_obj.py_modules[file_name].get_module_content():
                    fl_to_wr.write(value)
                fl_to_wr.write(constant.SINGLE_NEW_LINE)
                msg = "-- Pom processed and created : {}:--".format(
                    file_to_save)
                logger.info(msg)
        except Exception as error:
            logger.error(error)

    def print_pom(self, class_name, py_builder_obj):
        print("<<<<<<<<<<<<<<------------ Printing processed POM {}:------------------->>>>>>>>>>>>>>>>>>>".format(
            class_name))
        print(py_builder_obj[class_name].get_module_content())


def print_help():
    print("Supported commands: \n\tcommand - description ")
    for k, v in constant.SUPPORTED_COMMANDS.items():
        print("\t{} - {}".format(k, v))


if __name__ == '__main__':
    cmd_args = sys.argv[1:]
    valid_commands = constant.SUPPORTED_COMMANDS
    if len(cmd_args) > 0 and cmd_args[0] in valid_commands.keys():
        operation = cmd_args[0]
        if operation == "help":
            print_help()
        else:
            POMGenerator().execute(operation)
    else:
        print("Invalid command passed.")
        print_help()
