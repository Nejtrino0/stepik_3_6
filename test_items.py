from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Test_items:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

    def test_items_f(self, browser):
        browser.get(Test_items.link)
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#add_to_basket_form > button")))
        assert button, "Отсутствует кнопка добавления к корзину или она не активна"
