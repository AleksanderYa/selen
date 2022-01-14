from browser_class import Browser



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



