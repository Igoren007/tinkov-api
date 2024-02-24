import telebot
import requests

bot_api_tinkoff = telebot.TeleBot('')

from telebot import types

#igoren_tinkoff_api_bot
#curl localhost:8888/total

def get_total_money(url):

    resp = requests.get(url)
    return str(resp.text)


@bot_api_tinkoff.message_handler(commands=['start'])
def startBot(message):
    first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет! Показать баланс портфеля?"
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text = 'Да', callback_data='show')
    markup.add(button_yes)
    bot_api_tinkoff.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

@bot_api_tinkoff.callback_query_handler(func=lambda call:True)
def response(function_call):
    if function_call.message:
        if function_call.data == "show":
            second_mess = get_total_money("http://localhost:8888/total")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://timeweb.cloud/"))
            bot_api_tinkoff.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            bot_api_tinkoff.answer_callback_query(function_call.id)


bot_api_tinkoff.infinity_polling()