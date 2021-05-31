import telebot
import requests
import re
import os
from twilio.rest import Client
import pyrebase
from W13SCAN.api import Scanner
bot = telebot.TeleBot("Replace this with telegram bot father key", parse_mode=None)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    a = message.text
    b = a.split('@')
    print(b)
    global x
    global y
    global z
    global q
    chatt = message.chat.id
    if(b[0] == "/start"):
        bot.reply_to(message, "Welcome to is_vulnerable bot ")
    elif(b[0] == "/website"):
        x = b[1]
        scanner = Scanner(threads=20)
        scanner.put(x)
        y = scanner.run()
        print(x)
        bot.reply_to(message, str(y))
   
bot.polling()
