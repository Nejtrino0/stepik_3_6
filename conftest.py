import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# def pytest_addoption(parser):
#     parser.addoption('--language', action='store', default='fr',
#                      help="Choose language")
#     parser.addoption('--browser_name', action='store', default='chrome',
#                      help="Choose browser: chrome or firefox")


# @pytest.fixture(scope="function")
# def browser(request):
#     browser = None
#     browser_name = request.config.getoption("browser_name")
#     language = request.config.getoption("language")
#     if language == None:
#         raise pytest.UsageError("--Choose language")
#     elif browser_name == "chrome":
#         print("\nstart chrome browser for test..")
#         options = Options()
#         options.add_experimental_option('prefs', {'intl.accept_languages': language})
#         browser = webdriver.Chrome(options=options)
#     elif browser_name == "firefox":
#         print("\nstart firefox browser for test..")
#         fp = webdriver.FirefoxProfile()
#         fp.set_preference("intl.accept_languages", language)
#         browser = webdriver.Firefox(firefox_profile=fp)
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser = None
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    if not language:
        language = 'en'
    elif browser_name == "chrome":
        print("\nstart chrome browser for test..")
        # options.add_argument('headless')
        # options.add_argument('window-size=1920x935')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        print(language)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()

        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
        print(language)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
