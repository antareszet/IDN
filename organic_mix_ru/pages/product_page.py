import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:
    product_name = '//*[@id="bx_117848907_5247_title"]'  # локатор названия товара
    button_in_cart = '//a[@class="btn btn-link"]'  # локатор кнопки "В корзину"
    button_cart = '//*[@id="bx_basketFKauiI"]/div[1]'  # локатор Корзины
    button_place_order = '//*[@id="bx_basketFKauiI"]/div[2]/a'

    # GETTERS:
    def get_button_place_order(self):  # геттер кнопки "оформить заказ"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_place_order)))

    def get_cart(self):  # геттер кнопки " в Корзину"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))

    def get_button_in_cart(self):  # геттер кнопки " в Корзину"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_in_cart)))

    def get_product_name(self):  # геттер названия товара
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_name)))

    # Actions:
    def click_place_order(self):  # клик на оформить заказ"
        self.get_button_place_order().click()
        print('Click place an order')

    def click_cart(self):  # клик на корзину"
        self.get_cart().click()
        print('Click Cart')

    def click_button_in_cart(self):  # клик на кнопку "В корзину"
        # action = ActionChains()
        # action.move_to_element(self.get_button_cart()).perform()
        # time.sleep(1)
        self.get_button_in_cart().click()
        time.sleep(1)
        print('Click button IN CART')

    # Methods:
    def select_button_in_cart(self):  # метод добавление товара в корзину
        Logger.add_start_step(method='select_button_in_cart')
        self.get_current_url()
        self.assert_word(self.get_product_name(), 'Удобрение для хвойных Органик Микс 25 кг')
        self.click_button_in_cart()
        self.click_cart()
        self.click_place_order()
        Logger.add_end_step(url=self.driver.current_url, method='select_button_in_cart')

    def select_button_in_cart2(self):  # метод добавление товара в корзину
        Logger.add_start_step(method='select_button_in_cart2')
        self.get_current_url()
        self.click_button_in_cart()
        self.click_cart()
        self.click_place_order()
        Logger.add_end_step(url=self.driver.current_url, method='select_button_in_cart2')


