from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class Browser:

    _web_driver = None

    @classmethod
    @property
    def get_driver(cls) -> WebDriver:
        if cls._web_driver is None:
            cls._web_driver = cls._start_new_instance()
        return cls._web_driver

    @staticmethod
    def _start_new_instance() -> WebDriver:
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        return webdriver.Chrome(options=options)
