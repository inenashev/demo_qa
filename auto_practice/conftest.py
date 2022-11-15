import time

import pytest
from selenium import webdriver
from selenium.webdriver import Chrome,ChromeOptions
# create data-generator

@pytest.fixture()
def driver(request):
    # someday where will be options
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
