import telebot
from work import Switch

class Bot:
    TOKEN = '1342963300:AAGBnoqmIQ63KpcVMa9QuPgF_RtF_HXhwEU'
    CHAT_ID = 428637454
    TEXT = 'Hi'
    def __init__(self):
        self.bot = telebot.TeleBot(Bot.TOKEN, parse_mode=None)
        self.types = telebot.types
        self.browser = Switch()


    def send_message_to_telega(self):
        self.text = self.browser.turn_on()
        self.bot.send_message(Bot.CHAT_ID, self.text)

    def send_message(self, text):
        self.bot.send_message(Bot.CHAT_ID, text)


bot = Bot()
bot.send_message_to_telega()