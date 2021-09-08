from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Select a language')


@pytest.fixture(scope='function')
def browser(request):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': request.config.getoption('language')})
    print('\nStarting a browser')
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nQuit from browser')
    browser.quit()
