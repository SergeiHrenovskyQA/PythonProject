from utils.logger.logger import Logger
from web_elements.base_gui_element import BaseGuiElement


class Link(BaseGuiElement):

    def __init__(self, xpath: str, name: str):
        self.__logger = Logger(__name__).get_logger()
        super().__init__(xpath, name)
