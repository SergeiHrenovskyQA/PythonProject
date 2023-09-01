from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from enums.properties import Properties
from utils.browser.browser import Browser
from utils.file.local_file_utils import LocalFileUtils


class Waiter:

    DEFAULT_TIME_OUT = int(LocalFileUtils.json_get_field(Properties.PROPERTIES_FILE_PATH.value,
                                                         Properties.DEFAULT_TIME_OUT.value))
    MIDDLE_TIME_OUT = int(LocalFileUtils.json_get_field(Properties.PROPERTIES_FILE_PATH.value,
                                                        Properties.MIDDLE_TIME_OUT.value))
    LOW_TIME_OUT = int(LocalFileUtils.json_get_field(Properties.PROPERTIES_FILE_PATH.value,
                                                     Properties.LOW_TIME_OUT.value))

    def wait_for(self, func: callable, timeout: int = None) -> bool:
        try:
            return self.get_web_driver_waiter(timeout).until(self, func())
        except TimeoutException:
            return False

    def get_web_driver_waiter(self, timeout: int = None) -> WebDriverWait:
        timeout = self.DEFAULT_TIME_OUT if timeout is None else timeout
        return WebDriverWait(Browser.get_driver, timeout)
