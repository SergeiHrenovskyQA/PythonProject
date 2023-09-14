from enums.properties import Properties
from page_objects.euronews_main_page import EuronewsMainPage
from page_objects.forms.agreement_form import AgreementForm
from page_objects.news_letters_page import NewsLettersPage
from utils.browser.browser import Browser
from utils.file.local_file_utils import LocalFileUtils
from utils.logger.logger import Logger
from utils.waiter.waiter import Waiter


class EuronewsMainPageSteps:

    def __init__(self):
        self.__logger = Logger(__name__).get_logger()
        self.__url = LocalFileUtils.json_get_field(Properties.PROPERTIES_FILE_PATH.value, Properties.URL.value)
        self.euronews_page = EuronewsMainPage()
        self.agreement_form = AgreementForm()
        self.news_letters = NewsLettersPage()

    def open_main_page(self):
        self.__logger.info("Open main page")
        Browser().get(self.__url)
        if self.agreement_form.is_opened(Waiter().MIDDLE_TIME_OUT):
            self.agreement_form.click_agree_and_close()
        assert self.euronews_page.is_opened(), "Euronews main page is not opened"

    def click_news_letters_link(self):
        self.__logger.info("Follow the link 'Newsletters' in the header")
        self.euronews_page.click_news_letters()
        assert self.news_letters.is_opened(), "Euronews main page is not opened"
