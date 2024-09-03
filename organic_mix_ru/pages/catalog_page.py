import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Catalog_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:
    product_2_button = '//*[@id="bx_3966226736_23164_0f73996d13437b0b91038138616a89fe_pict"]'  # локатор продукта для метода выбора из меню
    product_button = '//*[@id="bx_3966226736_5255_4acf0f176831c66031059fe22bcc4d9c_pict"]'  # локатор продукта
    button_accept = '//*[@id="catalog_filter_mbuttons"]/button'  # локатор кнопки Применить
    radio_button_filter = '/html/body/div[4]/main/div/div[1]/div[1]/div/div/form/div[1]/div[2]/div/div[16]/label'  # локатор кнопки фильтра

    # GETTERS:
    def get_product_2_button(self):  # геттер продукта"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_2_button)))

    def get_product_button(self):  # геттер продукта"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_button)))

    def get_button_accept(self):  # геттер кнопки "Применить"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_accept)))

    def get_radio_button_filter(self):  # геттер кнопки выбора фильтра
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.radio_button_filter)))

    # Actions:

    def click_product_2(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_product_2_button())
        self.get_product_2_button().click()
        print('click Product')

    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0, 800);")
        print("scroll page")

    def move_to_product_button(self):  # двигаемся к продукту
        action = ActionChains(self.driver)
        action.move_to_element(self.get_product_button())
        self.get_product_button().click()
        time.sleep(1)
        print('click product')

    def click_button_accept(self):  # клик "применить""
        action = ActionChains(self.driver)
        action.move_to_element(self.get_button_accept())
        time.sleep(1)
        self.get_button_accept().click()
        print('click Button Accept')

    def click_radio_button_filter(self):  # выбор по фильтру"
        self.get_radio_button_filter().click()
        print('click Filter Button')

    # Methods:
    def select_filter(self):  # метод выбора фильтра
        Logger.add_start_step(method='select_filter')
        self.get_current_url()
        self.assert_url('https://organic-mix.ru/catalog/')
        self.click_radio_button_filter()
        time.sleep(1)
        self.click_button_accept()
        time.sleep(1)
        self.get_current_url()
        self.move_to_product_button()
        Logger.add_end_step(url=self.driver.current_url, method='select_filter')

    def select_product(self):
        Logger.add_start_step(method='select_product')
        self.get_current_url()
        self.scroll_page()
        self.click_product_2()
        Logger.add_end_step(url=self.driver.current_url, method='select_product')
