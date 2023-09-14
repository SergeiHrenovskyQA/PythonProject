from page_objects.base_page import BasePage
from web_elements.button import Button


class AgreementForm(BasePage):
    agree_and_close_button = Button("//button[contains(@aria-label, 'Agree and close')]", "Agree and close button")

    def __init__(self):
        super().__init__('''//div[contains(@class, 'consent-popup')]
        //div[contains(@aria-label, 'Consent Management')]'''.replace('\n', ''), "Agreement form")

    def click_agree_and_close(self):
        self.agree_and_close_button.click()
