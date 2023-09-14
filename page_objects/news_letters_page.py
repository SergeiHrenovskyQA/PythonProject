from typing import List

from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.forms.subscription_plan_form import SubscriptionPlanForm
from utils.browser.browser import Browser


class NewsLettersPage(BasePage):

    def __init__(self):
        super().__init__("//section[contains(@id, 'newletters')]", "News letters page")

    @staticmethod
    def get_subscription_plan_forms() -> List[SubscriptionPlanForm]:
        subscription_plans = Browser().find_elements(By.XPATH, SubscriptionPlanForm().get_base_xpath())
        return [SubscriptionPlanForm(subscription_plan) for subscription_plan in subscription_plans]
