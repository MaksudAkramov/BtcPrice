import requests
import json
import telebot
import config
from telebot import types
import time
import token

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('🤖Send Bitcoin rate')
    markup.row('🤖Sending Bitcoin every hour')

    bot.send_message(message.chat.id, "Добро пожаловать!", reply_markup=markup)


def get_btc(url):
    j = requests.get(url)
    data = json.loads(j.text)
    temp = data['result']['Ask']
    price ='Now BTC = ' + str(temp)+"$"
    return price

@bot.message_handler(content_types=['text'])
def give_info(message):
    print(message.chat.type)
    
    if message.chat.type == 'private':
        print('Btc')
        url = 'https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC'
        if message.text == '🤖Send Bitcoin rate':
            price = get_btc(url)
            bot.send_message(message.chat.id, price)
            
if message.text == '🤖Sending Bitcoin every hour':
    @bot.message_handler(content_types=['text'])
    def give_info_everyhour(message):
        print(message.chat.type)
        
        # send_message()  
        # time.sleep(60)
        
        if message.chat.type == 'private':
            print('Btc')
            url = 'https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC'
            
            
            price = get_btc(url)
            bot.send_message(message.chat.id, price)
            time.sleep(60)

