from pytest import fixture
from utils.browser.browser import Browser


@fixture()
def browser():
    yield Browser().get_driver
    Browser().get_driver.quit()
