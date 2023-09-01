from web_elements.label import Label


class BasePage:

    def __init__(self, xpath: str, name: str):
        self.xpath = xpath
        self.name = name

    def is_opened(self) -> bool:
        page = Label(self.xpath, self.name)
        return page.is_displayed()
