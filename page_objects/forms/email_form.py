from page_objects.base_page import BasePage


class EmailForm(BasePage):

    def __init__(self):
        super().__init__('''//form[@id='register-newsletters-form']'''.replace('\n', ''),
                         "Email register form")
