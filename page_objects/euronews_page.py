from page_objects.base_page import BasePage


class EuronewsPage(BasePage):
    def __init__(self, xpath: str, name: str):
        super().__init__(xpath, name)
