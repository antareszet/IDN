import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import Cart_page
from pages.main_page import Main_page
from pages.product_page import Product_page
from pages.order_make_page import Order_make_page


def test_buy_product_search():  # тест покупки товара по поиску
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_argument('--headless')
    options.add_argument('—disable-gpu')
    options.add_argument("disable-popup-blocking")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--disable-extensions")
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--ignore-ssl-errors')
    options.add_argument(
        'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"')
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print('Start Test BUY PRODUCT by Search')

    mp = Main_page(driver)
    mp.select_button_product()

    pp = Product_page(driver)
    pp.select_button_in_cart()

    cp = Cart_page(driver)
    cp.check_cart()

    omp = Order_make_page(driver)
    omp.check_order()

    driver.close()

    print('FINISH Test')
