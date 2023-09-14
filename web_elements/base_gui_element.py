from typing import List

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from utils.browser.browser import Browser
from utils.logger.logger import Logger
from utils.waiter.waiter import Waiter
from utils.web_element_utils.web_element_utils import WebElementUtils


class BaseGuiElement:

    web_element = None

    def __init__(self, web_element_or_xpath, name: str = ''):
        self.__logger = Logger(__name__).get_logger()
        self.name = name
        if isinstance(web_element_or_xpath, str):
            self.locator = web_element_or_xpath
        elif isinstance(web_element_or_xpath, WebElement):
            self.web_element = web_element_or_xpath
            self.locator = WebElementUtils.get_absolute_xpath(web_element_or_xpath)
        else:
            raise ValueError("Invalid arguments for web element constructor")

    def is_displayed(self, timeout: int = None) -> bool:
        self.__logger.info(f"Checking element isDisplayed: {self.name}")
        try:
            return self.__get_web_element(timeout).is_displayed()
        except NoSuchElementException:
            return False

    def is_clickable(self, timeout: int = None):
        self.__logger.info(f"Checking element clickable: {self.name}")
        return self.__get_web_element(timeout).is_enabled()

    def click(self, timeout: int = None):
        self.__logger.info(f"Click on element: {self.name}")
        self.__get_web_element(timeout).click()

    def find_child_element(self, xpath: str, timeout: int = None) -> WebElement:
        self.__logger.info(f"Find child element for '{self.name}' by xpath '{xpath}'")
        try:
            Waiter().get_web_driver_waiter(timeout).until(lambda _: len(self.__find_child_elements(xpath)) > 0)
            return self.__find_child_elements(xpath)[0]
        except TimeoutException:
            raise NoSuchElementException(f"Child element for '{self.name}' by xpath '{xpath}' is not found")

    def __get_web_element(self, timeout: int = None) -> WebElement:
        if self.web_element is not None:
            return self.web_element
        try:
            Waiter().get_web_driver_waiter(timeout).until(lambda _: len(self.__find_elements()) > 0)
            return self.__find_elements()[0]
        except TimeoutException:
            raise NoSuchElementException(f"Element '{self.name}' is not found")

    def __find_elements(self) -> List[WebElement]:
        return Browser().find_elements(By.XPATH, self.locator)

    def __find_child_elements(self, xpath: str) -> List[WebElement]:
        return self.__get_web_element().find_elements(By.XPATH, xpath)
