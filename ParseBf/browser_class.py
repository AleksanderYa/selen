from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Browser:
    PATH = 'D:\chromedriver.exe'
    # PATH = '/home/pi/Desktop/selenium/cromedriver/chromedriver'
    SITE = 'https://www.betfair.com/exchange/plus/inplay/football'
    FIND_TABLE = 'coupon-table'
    FIND_MARKET = 'mod-event-line'
    MARKET_VOLUME = 'matched-amount-value'
    NAME_MARKET = 'name'
    PLAYER_2 = 'away'
    PLAYER_1 = 'home'
    TIME_PLAY = 'middle-label'

    def __init__(self):
        self.chrome_options = Options()
        self.changer = Changer_types()
        self.chrome_options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(self.PATH, options=self.chrome_options)
        self.driver.wait = WebDriverWait(self.driver, 2)
        self.inplay_markets = []
        self.soonplay_markets = []

    def connect(self):
        print(f'Connect to:{self.SITE}')
        try:
            self.driver.get(self.SITE)
            print(f'Connect is DONE')
            sleep(2)
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
        self.result = _list
        for count, value in enumerate(self.result):
            try:
                value.find_element_by_class_name(self.TIME_PLAY).text
            except NoSuchElementException:
                delat = self.result.pop(count)
                print(delat)
        return self.result

    def inplay_market(self):
        self.__find_markets()
        result = self.inplay_markets.find_elements_by_class_name(self.FIND_MARKET)
        return result

    def soonplay_market(self):
        self.__find_markets()
        result = self.soonplay_markets.find_elements_by_class_name(self.FIND_MARKET)
        return result

    def view(self, _list: list):
        self.text_list = [f'Date: {datetime.today().day}.{datetime.today().month}.{datetime.today().year}\n' ]
        for i in _list:
            try:
                self.in_time = i.find_element_by_class_name(self.TIME_PLAY).text
                self.home_score = i.find_element_by_class_name(self.PLAYER_1).text
                self.away_score = i.find_element_by_class_name(self.PLAYER_2).text
                self.amaunt = i.find_element_by_class_name(self.MARKET_VOLUME).text ###
                self.amaunt_int = self.changer.to_int(self.amaunt)
                self.runners = i.find_elements_by_class_name(self.NAME_MARKET)
                self.home_runner = self.runners[0].text
                self.away_runner = self.runners[1].text
                self.text = f'{self.amaunt}\n{self.in_time}\n' \
                       f'{self.home_score} {self.home_runner}\n{self.away_score} {self.away_runner}\n\n'
                self.text_list.append(self.text)

            except:
                print('error')
        self.text_join = ' '.join(self.text_list)
        return self.text_join

class Changer_types:
    def __del_charge(self, text:str):
        return text[1:]

    def __replace_dot(self, _):
        text = self.__del_charge(_)
        res = text.replace(',', '')
        return res

    def to_int(self, _):
        text = int(self.__replace_dot(_))
        return text

class Tst:
    @staticmethod
    def hi():
        print('Hi')
        return 'Hi'