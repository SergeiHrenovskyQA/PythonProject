from pytest import fixture
from utils.browser.browser import Browser


@fixture(scope="session")
def browser():
    yield Browser()
    Browser().quit()
