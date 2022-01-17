from browser_class import Browser
from django_q.tasks import schedule
from telegram_bot import Bot


class Switch:
    def __init__(self):
        self.__browser = Browser()

    def turn_on(self):
        self.__browser.connect()
        self.__inplay = self.__browser.inplay_market()
        self.__soonplay = self.__browser.soonplay_market()
        self.__inplay_sorted = self.__browser.sort_markets(self.__inplay)
        # self.soonplay_sorted = browser.sort_markets(soonplay)
        self.res = self.__browser.view(self.__inplay_sorted)
        print(self.res)
        return self.res

    def turn_off(self):
        self.__browser.end()

class Scheduller:
    def __init__(self):
        self.bot = Bot()

    def go_sched(self):
        schedule(self.bot.send_message_to_telega(), schedule_type='I', minutes=1, repeats=-1)



sched = Scheduller()
sched.go_sched()