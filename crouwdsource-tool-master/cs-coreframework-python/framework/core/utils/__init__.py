import os
from pathlib import Path

conf_file = str(Path(os.getcwd()).parent)

# out_file_location = conf_file + "/output"
# out_file_location_logs = conf_file + "/output/logs"
#
#
# def create_dir(parent, child):
#     os.mkdir(parent)
#     os.mkdir(child)
#
#
# def remove_create_dir(parent, child):
#     os.rmdir(parent)
#     create_dir(parent, child)
#
#
# try:
#     if os.path.exists(out_file_location):
#         remove_create_dir(out_file_location, out_file_location_logs)
#     else:
#         create_dir(out_file_location, out_file_location_logs)
# except Exception as e:
#     print("Error: %s : %s" % (out_file_location, e.strerror))
