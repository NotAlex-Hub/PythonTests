from selenium.webdriver.common.by import By

from conftest import driver


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def check_title_is(self, title):
        page_title = self.driver.find_element(By.CSS_SELECTOR, "h2")
        assert page_title.text == title, "Некорректный заголовок"