import os
import json


class LocalFileUtils:
    PATH_TO_THE_DIRECTORY_ONE_LEVEL_UP = ".."
    DIRECTORY_SEPARATOR = os.path.sep

    @staticmethod
    def json_get_field(file_path: str, field: str):
        absolute_path = LocalFileUtils.__get_absolut_main_directory_path()
        full_file_path = os.path.join(absolute_path, file_path)

        with open(full_file_path, 'r') as json_file:
            data = json.load(json_file)
        return data[field]

    @staticmethod
    def __get_absolut_main_directory_path() -> str:
        return (os.getcwd()
                + LocalFileUtils.DIRECTORY_SEPARATOR
                + LocalFileUtils.PATH_TO_THE_DIRECTORY_ONE_LEVEL_UP)
