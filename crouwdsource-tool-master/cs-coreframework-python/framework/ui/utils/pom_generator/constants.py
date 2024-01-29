import os
from string import Template
# from environment import Paths
import logging

class Constant:
    CONFIG_FILE_PATH = os.getcwd() + "/properties/common/utility.config.cfg"
    # CONFIG_FILE_PATH = os.path.abspath('../../../ui_pytest/properties/common/utility.config.cfg')
    NOT_APPLICABLE = 'NA'
    DEFAULT_PROJECT_DIR = "ui_pytest"
    DEFAULT_POM_DIR = "pageobjects"

    SUPPORTED_COMMANDS = {"validate":"to read the json file and validating it",
                          "write":"to write the output files after reading and validating the json files",
                          "v":"shortcut for validate command",
                          "w":"shortcut for write command",
                          "help":"To show the available command"}

    # Logging format
    LOG_LEVEL = logging.INFO
    FRMT_STR = "%(asctime)s: %(levelname)s: %(funcName)s: Line:%(lineno)d %(message)s"
    DATE_STR = "%d/%m/%y %I:%M:%S %p"  # Date Format changed from default (m-d-y ) to (m/d/y)
    LOG_FILE_NAME = os.getcwd() + "/Reports/logs/utility/output.log"
    # LOG_FILE_NAME = '../../../ui_pytest/Reports/logs/utility/output.log'


    ## JSON File related constants.
    SIZE_ZERO = 0

    # Json input keys
    ELEMENT_TYPE = 'elementType'
    ELEMENT_NAME = 'elementName'
    ELEMENT_ACTION_METHODS = 'elementActionMethods'
    LOCATOR_IDENTIFIER_TYPE = 'locatorIdentifierType'
    LOCATOR_IDENTIFIER_VALUE = 'locatorIdentifierValue'
    LOCATOR_TYPE_VALUE_SEPARATOR = '|'
    ELEMENT_VERFICATION_METHODS = 'elementVerificationMethods'
    PAGE_NAME = 'pageName'
    OPERATION = 'operation'
    LOCATERS = 'locators'

    PARENT_CLASS_NAME = 'parentClassName'
    CHILD_CLASS_NAMES = 'childClassNames'


    # element types : Needs to update if any new element type is added
    WEB_ELEMENT_TYPES = {
        'TextBox': 'tb',
        'Link': 'link',
        'Button': 'btn',
        'Image': 'img',
        'CheckBox': 'chk',
        'RadioButton': 'rbtn',
        'DropDown': 'ddn',
        'ComboBox': 'cmb',
        'TextArea': 'ta',
        'Iframe': 'ifr',
        'Label': 'lb',
        'Div': 'div'}

    # Element and corresponding supported action methods mapping
    WEB_ELE = {
        # elementType : supported elementActionMethods
        "TextBox": "getValue,clearText,setText,getAttribute",
        "DropDown": "selectByIndex,selectByValue,selectByText,getSelectedValue,getSelectedText",
        "Link": "click,getText",
        "Button": "click,doubleClick,getAttribute,getText",
        "Image": "doubleClick,click,getAttribute",
        "CheckBox": "check,unCheck,isChecked,getAttribute",
        "RadioButton": "selectRadioButton,isRadioButtonSelected,getAttribute",
        "ComboBox": "selectByIndex,selectByValue,selectByText,getAllSelectedValues,getAllSelectedTexts,deselectByIndex,deselectByValue,deselectByText,deselectAll",
        "TextArea": "getValue,clearText,setText",
        "Label": "getText",
        "Div": "click,getText,getAttribute",
        "Iframe": "switchToIframeByIndex,switchToIframeByElement,switchToParentFrame,switchToDefaultContent"
    }

    '''
    FUN_MAP is dictionary with json input is key and basemethods and corresponding parameters
     as a string with coma separated as value.
     Note: for every base method id is default hence we are considering to keep it.
     Example: for setText json input input_text is the base class method with one
     input parameter hence not considering to keep in below dictionary
    '''

    ACTION_MAP = {
        'setText': 'input_text,text',
        'getValue': 'get_value',
        'clearText': 'clear_value',
        'getText': 'get_text',
        'click': 'click',
        'doubleClick': 'double_click',
        'check': 'select_option',
        'unCheck': 'deselect_option',
        'isChecked': 'is_option_selected',
        'selectRadioButton': 'click',
        'isRadioButtonSelected': 'is_option_selected',
        'selectByIndex': 'drop_down_select_item_by_index,index',
        'selectByValue': 'drop_down_select_item_by_value,value',
        'selectByText': 'drop_down_select_item_by_text,text',
        'getSelectedValue': 'drop_down_get_selected_value',
        'getSelectedText': 'drop_down_get_selected_text',
        'getAllSelectedValues': 'combo_box_get_all_selected_values',
        'getAllSelectedTexts': 'combo_box_get_all_selected_texts',
        'deselectByIndex': 'combo_box_deselect_item_by_index,index',
        'deselectByValue': 'combo_box_deselect_item_by_value,value',
        'deselectByText': 'combo_box_deselect_item_by_text,text',
        'deselectAll': 'combo_box_deselect_all_items',
        #'get' :'drop_down_select_item_by_id',
        # :'drop_down_select_item_by_value,value',
        # :'drop_down_select_item_by_text,text',
        #:'drop_down_deselect_item_by_id,id',
        #:'drop_down_deselect_item_by_value,value',
        #:'drop_down_deselect_item_by_text,text',
        #:'is_drop_down_multiple_select'
        #:'drop_down_deselect_all_items',
        'getAttribute': 'get_attribute,attribute',
        'switchToIframeByIndex': 'switch_to_iframe_by_index,index',
        'switchToIframeByElement': 'switch_to_iframe_by_element',
        'switchToParentFrame': 'switch_to_parent_frame',
        'switchToDefaultContent': 'switch_to_default_content',
        #:'get_property,property',
        #:'get_value_of_css_property,css_property'
    }
    # Supported Verification methods in JSON
    WEB_ELE_VER_MAP = {
        # elementType : supported elementActionMethods
        "TextBox": "verifyElementValue,verifyIsElementPresent",
        "DropDown": "verifyIsElementPresent",
        "Link": "verifyElementText,verifyIsElementPresent",
        "Button": "verifyElementText,verifyIsElementPresent",
        "Image": "verifyIsElementPresent,verifyIsElementDisappeared",
        "CheckBox": "verifyIsElementPresent",
        "RadioButton": "verifyIsElementPresent",
        "ComboBox": "verifyIsElementPresent",
        "TextArea": "verifyElementValue,verifyIsElementPresent",
        "Label": "verifyElementAttribute,verifyElementText,verifyIsElementPresent",
        "Div": "verifyIsElementPresent",
        "Iframe": "verifyIsElementPresent"
    }

    # Verification method to core method mapping
    VER_METHOD_MAP = {
        'verifyElementValue': 'is_value,value',
        'verifyElementText': 'is_text,text',
        'verifyElementState': 'is_enabled',
        'verifyElementAttribute': 'is_attribute_value,attribute,value',
        'verifyIsElementPresent': 'is_present',
        'verifyIsElementDisappeared': 'is_disappeared'
    }

    METHOD_RETURN_MAP = {
        'setText': 'self',
        'getValue': 'return',
        'clearText': 'self',
        'getText': 'return',
        'click': 'self',
        'doubleClick': 'self',
        'check': 'self',
        'unCheck': 'self',
        'isChecked': 'return',
        'selectRadioButton': 'self',
        'isRadioButtonSelected': 'return',
        'selectByIndex': 'self',
        'selectByValue': 'self',
        'selectByText': 'self',
        'getAttribute': 'return',
        'getSelectedValue': 'return',
        'getSelectedText': 'return',
        'getAllSelectedValues': 'return',
        'getAllSelectedTexts': 'return',
        'deselectByIndex': 'self',
        'deselectByValue': 'self',
        'deselectByText': 'self',
        'deselectAll': 'self',
        'switchToIframeByIndex': 'self',
        'switchToIframeByElement': 'self',
        'switchToParentFrame': 'blank',
        'switchToDefaultContent': 'blank',
        'verifyElementValue': 'return',
        'verifyElementText': 'return',
        'verifyElementState': 'return',
        'verifyElementAttribute': 'return',
        'verifyIsElementPresent': 'return',
        'verifyIsElementDisappeared': 'return'
    }







    # Template strings

    # user defined space for indentation and new line
    SINGLE_TAB = '    '
    DOUBLE_TAB = str(SINGLE_TAB * 2)
    SINGLE_NEW_LINE = '\n'
    DOUBLE_NEW_LINE = '\n\n'
    PASS = "pass"
    ACTION_POM_DIR_NAME = "actions"
    VERIFICATION_POM_DIR_NAME = "verifications"

    BASE_CLASS_NAME = 'BasePage'
    BASE_CLASS_PATH = "from framework.ui.base.base_page import BasePage" + SINGLE_NEW_LINE
    BASE_CLASS_PATH_FOR_VERIFICATION = Template('from ${project_folder_name}.${pom_dir_name}.actions.${page_name} import ${page_name}' + SINGLE_NEW_LINE)
    BASE_CLASS_NAME_POSTFIX_TEXT = "Verification"

    DYNAMIC_VAR_REPLACER = "%s"
    DYNAMIC_VAR_POSTFIX = "_dynamic"
    DYNAMIC_NTH_PARAMETER = ", dynamic_text"
    DYNAMIC_VAR_FORMAT = ".format(dynamic_text)"


    CLASS_INITIALIZATION_STATEMENT = Template("class ${class_name}(${parent_class_name}):")
    CLASS_VARIABLE_INITIALIZATION_STATEMENT = Template('${variable_name} = "${variable_value}"')

    CLASS_CONSTRUCTOR_METHOD_INITIALIZATION = SINGLE_TAB + "def __init__(self, driver):"
    CLASS_CONSTRUCTOR_METHOD_SUPER_STATEMENT = Template(DOUBLE_TAB + "super(${class_name}, self).__init__(driver)")

    CLASS_METHOD_INITIALIZATION = Template(SINGLE_TAB + "def ${method_name}_${element_name}(self${parameters}):")
    CLASS_METHOD_CALL_STATEMENT = Template(DOUBLE_TAB + "${return_option}self.${associated_obj}.${method_name}(self.${element_name}${parameters})")
    CLASS_METHOD_CALL_STATEMENT_NO_PARAM = Template(DOUBLE_TAB + "${return_option}self.${associated_obj}.${method_name}()")
    CLASS_METHOD_RETURN_STATEMENT = Template(DOUBLE_TAB + "return ${return_obj}")


    # JSON PROPERTIES

    JSON_POM_KEYS = ["pageName", "operation","parentClassName","childClassNames","locators"]
    JSON_LOCATOR_KEYS = ["elementName","elementType","locatorIdentifierType","locatorIdentifierValue","elementActionMethods","elementVerificationMethods"]
    JSON_LOCATOR_IDENTIFIER_TYPES = ['id','name','class_name','tag_name', 'xpath','css_selector','link_text','partial_link_text']

    # Function template
    DEF_STR = Template(
        SINGLE_TAB +
        "def ${action}_${element_name}(self$params):")
    COMM_STR = Template(
        DOUBLE_TAB +
        "# This is the function to perform ${action} on web element ${element_name}" + SINGLE_NEW_LINE)