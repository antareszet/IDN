import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:
    button_place_order = '//*[@id="basket-root"]/div[4]/div/div[2]/div[2]/div/div[2]/button[1]'

    # GETTERS:
    def get_button_place_order(self):  # геттер кнопки Оформить заказ"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_place_order)))

    # Actions:

    def click_button_place_order(self):  # клик оформить заказ"
        self.get_button_place_order().click()
        print('click Place Order')

    # Methods:
    def check_cart(self):
        Logger.add_start_step(method='check_cart')
        self.get_current_url()
        self.assert_url('https://organic-mix.ru/personal/cart/')
        self.click_button_place_order()
        Logger.add_end_step(url=self.driver.current_url, method='check_cart')
