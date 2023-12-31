from utils.logger.logger import Logger
from web_elements.base_gui_element import BaseGuiElement


class Label(BaseGuiElement):

    def __init__(self, web_element_or_xpath, name: str = ''):
        self.__logger = Logger(__name__).get_logger()
        super().__init__(web_element_or_xpath, name)
