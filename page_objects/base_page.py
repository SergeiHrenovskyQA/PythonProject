from web_elements.label import Label


class BasePage:

    def __init__(self, xpath: str, name: str):
        self.xpath = xpath
        self.name = name

    def is_opened(self, timeout: int = None) -> bool:
        return self._get_base_web_element().is_displayed(timeout)

    def get_base_xpath(self) -> str:
        return self.xpath

    def _get_base_web_element(self) -> Label:
        return Label(self.xpath, self.name)
