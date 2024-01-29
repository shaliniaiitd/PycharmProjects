Page Object Model Class Generator
Input   : Reads Json Formatted Data
Output  : POM Class python file

0. CD into your sub project folder
1. Mention absolute path of folder containing all pom json in properties->common->utility.config.cfg for variable "json_dir_path"
2. Mentioned absolute path of root dir in utility.config.cfg for variable "root_dir"
3. Mention test project folder name in utility.config.cfg for variable "project_folder_name"
4. Mention pom output dir name in utility.config.cfg for variable "pom_dir_name". It good to set path under ui\pageobjects

NOTE:  MAKE SURE TO RUN BELOW COMMAND FROM THE PATH WHERE properties and Reports DIR ARE PRESENT.

5. Now validate the pom json are valid or not using following command from project root dir.
    python <path_to_utility>\framework\ui\utils\pom_generator validate
6. To generate the Page objects at the desired place as per config using following command when no error occurred in validation
    python path_to_utility>\framework\ui\utils\pom_generator write
7.  SUPPORTED_COMMANDS = {"validate":"to read the json file and validating it",
                          "write":"to write the output files after reading and validating the json files",
                          "v":"shortcut for validate command",
                          "w":"shortcut for write command",
                          "help":"To show the available command"}
8.

config.cfg:
[common info]
json_dir_path =  C:\prj\crouwdsource-tool\cs-coreframework-python\ui_pytest_example\pagejsons\
root_dir = C:\prj\crouwdsource-tool\cs-coreframework-python\
project_folder_name = ui_pytest_example
pom_dir_name = pageobjects


Above listed parameters should be present with out any modification in config.cfg
you can change the path by giving any working path or NA or ' ';
json_dir_path is the source director path where *.json files are presented you can give any working directory path or NA or ''
pom_dir_path is the destination director path where *.py files are presented you can give any working directory path or NA or ''

if json_dir_path /pom_dir_path is NA or '' then tool will search for the json files in current working directory
where the script is presented and placed all the .py files in the same directory


Working Format of Json:
Below listed Json Formatted data is supported hence use the same as input
[
  {
    "pageName": "SearchResultsPage",
    "operation": "create",
    "parentClassName": "Parent_Class",
    "childClassNames": "NA",
    "locators": [
      {
        "elementName": "SearchItem",
        "elementType": "Image",
        "locatorIdentifierType": "xpath",
        "locatorIdentifierValue": "//img[@alt='Wilson NFL Super Grip Football']",
        "elementActionMethods": "click",
        "elementVerificationMethods": ""
      },
      {
        "elementName": "AddToCartButton",
        "elementType": "Button",
        "locatorIdentifierType": "xpath",
        "locatorIdentifierValue": "//input[@id='add-to-cart-button']",
        "elementActionMethods": "click",
        "elementVerificationMethods": ""
      }
    ]
  }

Note: if multiple class data is presented in the json file then multiple class(POM)
    files will be generated with with class name mentioned in json.