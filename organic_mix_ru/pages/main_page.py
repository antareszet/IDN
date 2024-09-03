import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):
    url = 'https://organic-mix.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:
    search_field = '//*[@id="h_upd"]/div[4]/a'  # локатор поля поиска
    search_field_input = '//*[@id="searchInput"]'  # локатор поля для ввода в поиск
    product_button = '//*[@id="bx_3966226736_5247_ec5d0e2cff91ab20debac17d8febe5be_title"]'  # локатор продукта
    button_catalog = '/html/body/header/div[1]/div/nav/ul/li[1]/a'  # локатор кнопки Каталог
    button_top_menu = '/html/body/header/div[1]/div/nav/ul/li[3]/a'  # локатор кнопки выбора каталока верхнего меню

    # GETTERS:
    def get_button_top_menu(self):  # геттер каталога"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_top_menu)))

    def get_button_catalog(self):  # геттер каталога"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_catalog)))

    def get_button_product(self):  # геттер продукта"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_button)))

    def get_search_field_input(self):  # геттер поля поиска"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_field_input)))

    def get_search_field(self):  # геттер поля поиска"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_field)))

    # Actions:
    def click_button_catalog(self):  # клик на товар"
        self.get_button_catalog().click()
        time.sleep(1)
        print('Click Product Button')

    def click_button_top_menu(self):  # клик на кнопку меню"
        self.get_button_top_menu().click()
        time.sleep(1)
        print('Click Menu Button')

    def input_search_field(self):  # ввод слова в поле поиска"
        self.get_search_field().click()
        time.sleep(1)
        self.get_search_field_input().send_keys('Хвойные')
        print('Input Word in Search Field')
        # time.sleep(1)

    def click_button_product(self):  # клик на товар"
        self.get_button_product().click()
        time.sleep(1)
        print('Click Product Button')

    # Methods:
    def select_button_product(self):  # метод быбора товара по поиску
        Logger.add_start_step(method='select_button_product')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_search_field()
        time.sleep(0.5)
        self.click_button_product()
        Logger.add_end_step(url=self.driver.current_url, method='select_button_product')

    def select_product_catalog(self):  # метод выбора товара из каталога
        Logger.add_start_step(method='select_product_catalog')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_button_catalog()
        Logger.add_end_step(url=self.driver.current_url, method='select_product_catalog')

    def select_product_by_menu(self):  # метод выбора товара из каталога
        Logger.add_start_step(method='select_product_by_menu')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_button_top_menu()
        Logger.add_end_step(url=self.driver.current_url, method='select_product_by_menu')

