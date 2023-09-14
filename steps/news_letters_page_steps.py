import random

from page_objects.forms.email_form import EmailForm
from page_objects.news_letters_page import NewsLettersPage
from utils.logger.logger import Logger


class NewsLettersPageSteps:

    def __init__(self):
        self.__logger = Logger(__name__).get_logger()
        self.newsLettersPage = NewsLettersPage()
        self.email_form = EmailForm()

    def choose_random_newsletter_subscription_plan(self):
        subscription_plan_forms = self.newsLettersPage.get_subscription_plan_forms()
        subscription_plan_form = random.choice(subscription_plan_forms)
        subscription_plan_form.click_select_this_newsletter_button()
        assert self.email_form.is_opened(), "Email register form is not appeared"
