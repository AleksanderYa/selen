import telebot
from time import sleep
from selenium.common.exceptions import TimeoutException
from ParseBf.work import Switch


class Bot:
    TOKEN = '1342963300:AAGBnoqmIQ63KpcVMa9QuPgF_RtF_HXhwEU'
    CHAT_ID = 428637454
    TEXT = 'Hi'

    def __init__(self):
        self.types = telebot.types
        self.browser = Switch()

    def send_message_to_telega(self):
        try:
            self.bot = telebot.TeleBot(Bot.TOKEN, parse_mode=None)
            self.text = self.browser.turn_on()
            self.bot.send_message(Bot.CHAT_ID, self.text)
            print('Massage is send')
            self.browser.turn_off()
        except TimeoutException:
            sleep(1)
            self.send_message_to_telega()

    def send_message(self, text):
        self.bot.send_message(Bot.CHAT_ID, text)


