from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from utils.browser.browser import Browser
from utils.logger.logger import Logger
from utils.waiter.waiter import Waiter


class BaseGuiElement:

    def __init__(self, locator: str, name: str):
        self.__logger = Logger(__name__).get_logger()
        self.locator = locator
        self.name = name
        self.web_element = WebElement

    def is_displayed(self, timeout: int = None) -> bool:
        self.__logger.info("Checking element isDisplayed: " + self.name)
        timeout = Waiter().LOW_TIME_OUT if timeout is None else timeout
        try:
            return self.__get_web_element(timeout).is_displayed()
        except NoSuchElementException:
            return False

    def __get_web_element(self, time_out: int = None) -> WebElement:
        try:
            Waiter().get_web_driver_waiter(time_out).until(lambda _: len(self.__find_elements()) > 0)
            return self.__find_elements()[0]
        except TimeoutException:
            raise NoSuchElementException("Element " + self.name + " is not found")

    def __find_elements(self):
        return Browser().get_driver.find_elements(By.XPATH, self.locator)
