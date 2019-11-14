

import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome('../chrome78/chromedriver.exe')

    #driver.implicitly_wait(5)


    driver.maximize_window()

    yield driver
    driver.quit()
