import os
from enum import Enum

from utils.file.local_file_utils import LocalFileUtils


class Properties(Enum):
    PROPERTIES_FILE_PATH = r"environment_properties{}properties.json".format(LocalFileUtils.DIRECTORY_SEPARATOR)
    URL = "url"
    DEFAULT_TIME_OUT = "default_time_out"
    MIDDLE_TIME_OUT = "middle_time_out"
    LOW_TIME_OUT = "low_time_out"
