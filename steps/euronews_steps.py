from enums.properties import Properties
from page_objects.euronews_page import EuronewsPage
from utils.browser.browser import Browser
from utils.file.local_file_utils import LocalFileUtils
from utils.logger.logger import Logger


class EuronewsSteps:

    def __init__(self):
        self.__logger = Logger(__name__).get_logger()
        self.__url = LocalFileUtils.json_get_field(Properties.PROPERTIES_FILE_PATH.value, Properties.URL.value)
        self.euronews_page = EuronewsPage("//body[@data-website='euronews']" +
                                          "//ul[contains(@class, 'section__nav')]" +
                                          "//strong[normalize-space()='Top tags']",
                                          "Euronews page")

    def open_main_page(self):
        self.__logger.info("Open main page")
        Browser.get_driver.get(self.__url)
        assert self.euronews_page.is_opened(), "Euronews main page is not opened"
