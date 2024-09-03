import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    '''Method Get Current Url'''

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current URL: {get_url}')

    '''Method Assert Word'''

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')

    '''Method Assert Price'''

    def assert_price(self, price, result):
        value_price = price.text
        assert value_price == result
        print('Good value PRICE!')

    '''Method Screenshot'''

    def get_screenshot(self):
        now_date = datetime.datetime.today().strftime('%Y.%m.%d.%H.%M.%S')
        # now_date = datetime.datetime.now(datetime.UTC).strftime('%Y.%m.%d.%H.%M.%S')
        print(now_date)
        name_screenshot = f'screenshot_{now_date}.png'
        self.driver.save_screenshot('C:\\Users\\User\\PycharmProjects\\organic_mix_ru\\screen\\' + name_screenshot)

    '''Method assert URL'''

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('GOOD value URL')
