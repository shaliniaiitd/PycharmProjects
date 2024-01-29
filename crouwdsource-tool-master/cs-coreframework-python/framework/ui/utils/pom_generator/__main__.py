import sys

from constants import Constant as constant
from auto_pom_generator import POMGenerator

def print_help():
    print("Supported commands: \n\tcommand - description ")
    for k, v in constant.SUPPORTED_COMMANDS.items():
        print("\t{} - {}".format(k, v))


cmd_args = sys.argv[1:]
valid_commands = constant.SUPPORTED_COMMANDS
if len(cmd_args) > 0 and cmd_args[0] in valid_commands.keys():
    operation = cmd_args[0]
    if operation == "help":
        print_help()
    else:
        POMGenerator().execute(operation)
        print("Please see logs in log file at {}".format(constant.LOG_FILE_NAME))
else:
    print("Invalid command passed.")
    print_help()