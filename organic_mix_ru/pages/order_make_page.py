import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Order_make_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:
    prod_name = '//*[@id="bx-soa-basket"]/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div[1]/a'  # локатор товара

    # GETTERS:
    def get_prod_name(self):  # геттер продукта"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.prod_name)))

    # Actions:

    # Methods:
    def check_order(self): # метод проверки товара + скрин(тест по поиску товара)
        Logger.add_start_step(method='check_order')
        self.get_current_url()
        self.assert_word(self.get_prod_name(), 'Удобрение для хвойных Органик Микс 25 кг')
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method='check_order')


    def check_order2(self): # метод проверки товара + скрин(тест выбора товара по фильтру)
        Logger.add_start_step(method='check_order2')
        self.get_current_url()
        self.assert_word(self.get_prod_name(), 'Удобрение для хвойных Органик Микс 850 гр.')
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method='check_order2')

    def check_order3(self): # метод проверки товара + скрин(тест выбора товара из меню)
        Logger.add_start_step(method='check_order3')
        self.get_current_url()
        self.assert_word(self.get_prod_name(),
                         'ЯЙЦЕХРУСТ универсальный – от вредителей на стадии яиц, личинок и куколок, 15 мл')
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method='check_order3')
