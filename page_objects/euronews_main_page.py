from page_objects.base_page import BasePage
from web_elements.link import Link


class EuronewsMainPage(BasePage):

    HEADER_XPATH = "//div[@class='o-site-header__top']"

    news_letters = Link(HEADER_XPATH + "//a[@aria-label='Newsletters']", 'Newsletters link')

    def __init__(self):
        super().__init__('''//body[@data-website='euronews']//ul[contains(@class, 'section__nav')]
            //strong[normalize-space()='Top tags']'''.replace('\n', ''), "Euronews page")

    def click_news_letters(self):
        self.news_letters.is_clickable()
        self.news_letters.click()
