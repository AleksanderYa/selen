# Testing

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# ----------------------------------------------------------------------------
PATH = 'D:\chromedriver.exe'
SITE = 'https://www.betfair.com/exchange/plus/inplay/football'


# ----------------------------------------------------------------------------

def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    driver = webdriver.Chrome(PATH, options=chrome_options)
    driver.wait = WebDriverWait(driver, 5)
    return driver


driver = init_driver()


# ----------------------------------------------------------------------------

def connect_to_site(
        driver,
        site=SITE
):
    try:
        driver.get(site)
        return driver
    except Exception as e:
        print('Connet_to_site', e)


# ----------------------------------------------------------------------------

def firs_search(
        find_name="coupon-table",
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


box = firs_search()
in_play_box = box[0]
soon_play_box = box[1]


# ----------------------------------------------------------------------------
def end(time: object, driver: object = driver) -> object:
    time.sleep(5)
    driver.quit()
    print('Session The end')



def main():
    time.sleep(0.5)
    li_in = in_play_box.find_elements_by_class_name('mod-event-line')
    time.sleep(0.5)
    li_end = soon_play_box.find_elements_by_class_name('mod-event-line')

    print('---------------FIND Li_in ----------------')
    print(li_in)
    print('---------------END Li_in ----------------')

    print('---------------FIND Li----------------')
    print(li_end)
    print('---------------END Li----------------')


    for i in li_in:
        print(i.text)
        print()
        print('--------------')
    end(time)

if __name__ == '__main__':
    main()
