import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


PATH = 'D:\chromedriver.exe'
SITE = 'https://www.betfair.com/exchange/plus/inplay/football'

def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    driver = webdriver.Chrome(PATH, options=chrome_options)
    driver.wait = WebDriverWait(driver, 5)
    return driver


def connect_to_site(
        driver,
        site=SITE
):
    try:
        driver.get(site)
        return driver
    except Exception as e:
        print('Connet_to_site', e)


def firs_search(
        find_name,
        driver=connect_to_site(driver)
):
    try:
        box = driver.wait.until(EC.presence_of_all_elements_located(
            (By.CLASS_NAME, find_name)))
        print('---------------FIND BOX----------------')
        print(box)
        print('---------------END BOX----------------')
        return box
    except Exception as e:
        print('firs_search', e)

def end(time: object, driver: object = driver) -> object:
    time.sleep(5)
    driver.quit()
    print('Session The end')

def ivent_info(ivetn):
    try:
        in_time = ivetn.find_element_by_class_name('middle-label').text
        home_score = ivetn.find_element_by_class_name('home').text
        away_score = ivetn.find_element_by_class_name('away').text
        runners = ivetn.find_elements_by_class_name('name')
        home_runners = runners[0].text
        away_runners = runners[1].text
        return [
            in_time,
            home_score,
            away_score,
            home_runners,
            away_runners
        ]
    except NoSuchElementException:
        pass
