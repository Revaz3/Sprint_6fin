import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    firefox = webdriver.Firefox()

    yield firefox
    firefox.quit()