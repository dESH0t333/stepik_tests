import pytest


from selenium import webdriver
from selenium.webdriver.common.by import By



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="ru")

@pytest.fixture(scope="function")
def browser(request):

    language = request.config.getoption("language") 
    browser = webdriver.Firefox()
    print("\nstart browser for test..")
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    #browser.quit()



    

