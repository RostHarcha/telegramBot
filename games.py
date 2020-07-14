import random
import tgbot

class games:
    bot = telebot.TeleBot(config.Token)

    games_keyb = telebot.types.ReplyKeyboardMarkup(True, True)
    games_keyb.row('Орел и Решка', 'Угадай число', 'Убей себя')

    game_EaT_keyb = telebot.types.ReplyKeyboardMarkup(True, True)
    game_EaT_keyb.row('Орел', 'Решка')

    def menu(message):
        bot.send_message(message.chat.id, 'Хуигры!', reply_markup=games_keyb)

    @bot.message_handler(content_types = ['text'])
    def game(message):
        if(message.text.lower() == 'орел и решка'):
            bot.send_message(message.chat.id, 'Орел и Решка')

        else:
            tgbot.start_message(message)

    bot.polling()
