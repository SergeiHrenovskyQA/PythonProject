from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class Browser:

    def __new__(cls) -> WebDriver:
        if not hasattr(cls, 'web_driver'):
            options = Options()
            options.add_argument("--start-maximized")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            cls.web_driver = webdriver.Chrome(options=options)
        return cls.web_driver
