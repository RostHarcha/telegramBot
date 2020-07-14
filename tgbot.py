
###hello_keyb = telebot.types.ReplyKeyboardMarkup(True, True)
###hello_keyb.row('Привет', 'Инфа')
##
###func_keyb = telebot.types.ReplyKeyboardMarkup(True, True)
###func_keyb.row('Игры', 'Инфа', 'Пока')
##
###def EaT_start(message):
##    bot.send_message(message.chat.id, 'Орел или Решка?', reply_markup=game_EaT_keyb)
##def EaT_game(message):
##    answ = random.choice(["орел", "решка"])
##
##    if message.text.lower() == answ:
##        bot.send_message(message.chat.id, 'Ты угадал!', reply_markup=func_keyb)
##        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAICv15YLjjxkB4qTa9GeFYQfVuKB5vTAAIFAAP8decePX_WoA6bqW0YBA', reply_markup=func_keyb)
##        print(message.from_user.first_name, ' выиграл.')
##    else:
##        bot.send_message(message.chat.id, 'Ты не угадал!')
##        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBv15YEdzvUG2gVj_zPQcptaXnnBzsAAIEAAP8deceBjYAARQFKpZuGAQ', reply_markup=func_keyb)
##        print(message.from_user.first_name, ' проиграл.')
##
##@bot.message_handler(commands = ['start'])
##def start_message(message):
##    bot.send_message(message.chat.id, 'Привет! Я - Rostislaww бот. Меня написал Бостик Рогачeв')
##    bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAMZXlfRH94kd8lJiS9PXSiYaEoqH9UAAvoAA3MaRAU8vIsYvUleiRgE', reply_markup=func_keyb)
##
##@bot.message_handler(content_types = ['text'])
##def send_text(message):
##    print(message.from_user.first_name, ' : ', message.text)
##
##    if message.text.lower() == 'привет':
##        start_message(message)
##
##    elif message.text.lower() == 'пока':
##        bot.send_message(message.chat.id, 'Пока! Я спать.')
##        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAIBJ15X_Un8HZ0H0WyL1kB5LoUhXfcaAAKRAANzGkQFwfUPdcbwFWcYBA')
##
##    elif message.text.lower() == 'игры':
##        games.menu(message)
##
##    elif message.text.lower() == 'орел и решка':
##        EaT_start(message)
##
##    elif message.text.lower() == 'орел' or message.text.lower() == 'решка':
##        EaT_game(message)
##
##    elif message.text.lower() == 'инфа':
##        bot.send_message(message.chat.id, 'Я - бот, созданный Ростиславом (vk.com/hackkerman). Он мой царь, бог, я его люблю. Тебя тоже люблю.')
##        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIB0l5YFseapJTMW-JdEqVubAF6uTPdAAICAAP8deceI3qxF1t3MnQYBA', reply_markup=func_keyb)
##
##    else:
##        bot.send_message(message.chat.id, 'Неизвестная команда.')
##        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBv15YEdzvUG2gVj_zPQcptaXnnBzsAAIEAAP8deceBjYAARQFKpZuGAQ', reply_markup=func_keyb)
##
##@bot.message_handler(content_types = ['sticker'])
##def return_sticker_id(message):
##    print(message.from_user.first_name, ' : ', 'STICKER ', message.sticker.emoji, message.sticker.file_id)

import telebot
import config
import stickers

bot = telebot.TeleBot(config.Token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Дороу. Я бот Виват-лидера 2019, полуфиналиста Региональной Невской лиги КВН, царя, бога и просто хорошего человека Ростислава Олеговича. А еще я люблю его стикерпак :)')
    bot.send_sticker(message.chat.id, stickers.confused_0)

@bot.message_handler(content_types=['sticker'])
def return_sticker_id(message):
    bot.send_message(message.chat.id, message.sticker.file_id)
    bot.send_message(message.chat.id, message.sticker.emoji)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
