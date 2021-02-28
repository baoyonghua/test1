import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


@pytest.fixture()
def init_driver():
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    # time.sleep(3)
    driver.quit()

