import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init_driver")
@pytest.mark.parametrize("data", ["测试", "自动化测试", "性能测试", "syp"])
def test_bd(data, init_driver):
    init_driver.get("https://www.baidu.com")
    ele = init_driver.find_element(By.ID, "kw")
    ele.send_keys(data)
    click_ele = init_driver.find_element(By.ID, "su")
    click_ele.click()
    assert "测试" in data


if __name__ == '__main__':
    pytest.main()
