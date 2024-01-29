import os


class Paths:
    ABS_PATH = os.path.abspath(__file__)
    BASE_DIR = os.path.dirname(ABS_PATH)
    FRAMEWORK = os.path.join(BASE_DIR, "framework")
    PROPERTIES = os.path.join(BASE_DIR, "properties")
    REPORTS = os.path.join(BASE_DIR, "reports")
