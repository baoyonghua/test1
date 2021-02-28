import time

import pytest
from selenium import webdriver


@pytest.fixture()
def init_driver():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(3)
    driver.quit()

