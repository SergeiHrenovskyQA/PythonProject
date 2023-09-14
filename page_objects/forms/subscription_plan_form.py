from selenium.webdriver.remote.webelement import WebElement

from page_objects.base_page import BasePage
from utils.web_element_utils.web_element_utils import WebElementUtils
from web_elements.label import Label


class SubscriptionPlanForm(BasePage):

    select_this_newsletter_xpath = ".//label[normalize-space()='Select this newsletter']"

    def __init__(self, web_element: WebElement = None):
        base_xpath = ("//form[@id='newsletters-form']//div[@class='bg-white shadow-lg']"
                      .replace('\n', '')) if (web_element is None)\
            else WebElementUtils.get_absolute_xpath(web_element)

        super().__init__(base_xpath, "Subscription plan form")

    def click_select_this_newsletter_button(self):
        self.__get_select_this_newsletter_button().click()

    def __get_select_this_newsletter_button(self) -> Label:
        web_element = self._get_base_web_element().find_child_element(self.select_this_newsletter_xpath)
        return Label(web_element, "Select this newsletter button")
