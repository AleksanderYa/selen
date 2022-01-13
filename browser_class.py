from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Browser:
    PATH = 'D:\chromedriver.exe'
    SITE = 'https://www.betfair.com/exchange/plus/inplay/football'
    FIND_TABLE = 'coupon-table'
    FIND_MARKET = 'mod-event-line'
    NAME_MARKET = 'name'
    PLAYER_2 = 'away'
    PLAYER_1 = 'home'
    TIME_PLAY = 'middle-label'

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(self.PATH, options=self.chrome_options)
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.inplay_markets = []
        self.soonplay_markets = []

    def connect(self):
        print(f'Connect to:{self.SITE}')
        try:
            self.driver.get(self.SITE)
            print(f'Connect is DONE')
        except Exception as e:
            print('Error', e)

    def end(self):
        sleep(2)
        self.driver.quit()
        print(f'Session from {self.SITE} The end')

    def __find_coupon_table(self):
        result = self.driver.wait.until(EC.presence_of_all_elements_located(
            (By.CLASS_NAME, self.FIND_TABLE)))
        return result

    def __find_markets(self):
        self.__coupon_table = self.__find_coupon_table()
        if len(self.__coupon_table) > 1:
            self.inplay_markets = self.__coupon_table[0]
            self.soonplay_markets = self.__coupon_table[1]
        elif len(self.__coupon_table) == 1:
            self.soonplay_markets = self.__coupon_table[0]
        else:
            raise NoSuchElementException('No have markets')

    def sort_markets(self, _list: list):
        result = _list
        for i in range(len(result) - 1):
            try:
                in_time = result[i].find_element_by_class_name(self.TIME_PLAY).text
            except NoSuchElementException:
                result.pop(i)
        return result

    def inplay_market(self):
        self.__find_markets()
        result = self.inplay_markets.find_elements_by_class_name(self.FIND_MARKET)
        result = self.sort_markets(result)
        return result

    def soonplay_market(self):
        self.__find_markets()
        result = self.soonplay_markets.find_elements_by_class_name(self.FIND_MARKET)
        result = self.sort_markets(result)
        return result

    def view(self, ii: list):
        for i in ii:
            try:
                self.in_time = i.find_element_by_class_name(self.TIME_PLAY).text
                self.home_score = i.find_element_by_class_name(self.PLAYER_1).text
                self.away_score = i.find_element_by_class_name(self.PLAYER_2).text
                self.runners = i.find_element_by_class_name(self.NAME_MARKET)
                print(f'{self.in_time} {self.home_score}-{self.away_score} {self.runners}')
            except:
                print('error')

