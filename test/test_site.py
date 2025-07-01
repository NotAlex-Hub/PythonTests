import time

from selenium.webdriver.common.by import By
from page.homepage import HomePage
from page.product import ProductPage
from conftest import driver


def test_open_galaxy_s6(driver):
    homepage = HomePage(driver)
    product = ProductPage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product.check_title_is("Samsung galaxy s6")

def test_two_monitor(driver):
    driver.get("https://demoblaze.com/")
    monitor_link = driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    monitor_link.click()
    time.sleep(2)
    monitors = driver.find_elements(By.CSS_SELECTOR, ".card")
    assert len(monitors) == 2
