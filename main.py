import sqlite3
import time

import telebot
import sys
import TgLib
import AvitoParser
basic_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=5)
basic_key = telebot.types.KeyboardButton(text='Назад')
basic_keyboard.row(basic_key)


buy_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=5)
buy_key = telebot.types.KeyboardButton(text='Проверить статус оплаты')
buy_keyboard.row(buy_key, basic_key)



stat_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=5)
stat_key1 = telebot.types.KeyboardButton(text='Показать последнюю покупку')
stat_key2 = telebot.types.KeyboardButton(text='Показать все покупки')
stat_keyboard.row(stat_key1, stat_key2)
stat_keyboard.row(basic_key)

otz_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=5)
otz_key = telebot.types.KeyboardButton(text='Показать все отзывы')
otz_keyboard.row(otz_key, basic_key)

tech_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=5)
tech_key = telebot.types.KeyboardButton(text='Посмотреть свои прошлые тз по заказу')
tech_keyboard.row(tech_key, basic_key)

order_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=5)
order_key1 = telebot.types.KeyboardButton(text='Консультация')
order_key2 = telebot.types.KeyboardButton(text='Покупка')
order_keyboard.row(order_key1, order_key2)
order_keyboard.row(basic_key)

order_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=5)
order_key1 = telebot.types.KeyboardButton(text='Консультация')
order_key2 = telebot.types.KeyboardButton(text='Покупка')
order_keyboard.row(order_key1, order_key2)
order_keyboard.row(basic_key)

welcome_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=5)
welcome_key1 = telebot.types.KeyboardButton(text='Найти не занятый телефон')
welcome_key2 = telebot.types.KeyboardButton(text='Посмотреть историю по телефонам')
welcome_key3 = telebot.types.KeyboardButton(text='Как юзать бота?')
welcome_keyboard.row(welcome_key1, welcome_key2)
welcome_keyboard.row(welcome_key3)

admin_stat_key1 = telebot.types.KeyboardButton(text='Новых пользователей за текущий День')
admin_stat_key2 = telebot.types.KeyboardButton(text='Новых пользователей за текущий Месяц')
admin_stat_key3 = telebot.types.KeyboardButton(text='Пользователей за текущий День')
admin_stat_key4 = telebot.types.KeyboardButton(text='Пользователей за текущий Месяц')

profile_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=5)
profile_key1 = telebot.types.KeyboardButton(text='Мои покупки')
profile_key2 = telebot.types.KeyboardButton(text='Дополнить тех.задание')
profile_key3 = telebot.types.KeyboardButton(text='Оставить отзыв')
profile_key4 = telebot.types.KeyboardButton(text='Позвать оператора')
profile_keyboard.row(profile_key1, profile_key2)
profile_keyboard.row(profile_key3, profile_key4)
profile_keyboard.row(basic_key)

admin_key1 = telebot.types.KeyboardButton(text='Статистика посещений')
admin_key2 = telebot.types.KeyboardButton(text='Рассылка')
admin_key3 = telebot.types.KeyboardButton(text='Бан лист')
admin_key4 = telebot.types.KeyboardButton(text='Редактирование фраз бота')
admin_spam_key1 = telebot.types.KeyboardButton(text='/start')
admin_spam_key2 = telebot.types.KeyboardButton(text='/back')
admin_spam_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=5)
admin_spam_keyboard.row(admin_spam_key1, admin_spam_key2)
bot = telebot.TeleBot('1827319074:AAE8YS7qzM2r9dkD22yVLPe28_FitbXoKVg')
TgLib.create_get_user_info_database('TestTelegramBd')
AvitoParser.avito_db()
# start
# profile
# orderbot
@bot.message_handler(commands=['start'])
def send_welcome(message):
    TgLib.get_user_info(bot, message)
    if message.text:
        if message.chat.id == 1421340487:
            while True:
                AvitoParser.avito('https://www.avito.ru/moskva/telefony/mobile-ASgBAgICAUSwwQ2I_Dc?cd=1&s=104', bot)
                time.sleep(100)
        gg = bot.send_message(message.chat.id, 'Сюда бот спамит новыми постави в авито\n'
                                               'Это называется рассылка епта\n',
                              reply_markup=welcome_keyboard)
        bot.register_next_step_handler(gg, menu_panel)
def menu_panel(message):
    TgLib.get_user_info(bot, message)
    if message.text == 'Найти не занятый телефон' or message.text == 'найти не занятый телефон':
        gg = bot.send_message(message.chat.id, 'Мы DI company\n'
                                               'Ты долбаеб')
        bot.register_next_step_handler(gg, menu_panel)
    elif message.text == 'Посмотреть историю по телефонам' or message.text == 'посмотреть историю по телефонам':
        gg = bot.send_message(message.chat.id, 'Мы DI company\n'
                                               'Мы заскамим весь мир!')
        bot.register_next_step_handler(gg, menu_panel)
    elif message.text == 'Как юзать бота?' or message.text == 'как юзать бота?':
        gg = bot.send_message(message.chat.id, 'Мы DI company\n'
                                               'Притворись мамонтом, чтобы мы заскамили весь мир!')
        bot.register_next_step_handler(gg, menu_panel)
#############################


def start_message(message):
    if message.text:
        TgLib.get_user_info(bot, message)
        # my id 1421340487
        # kirill 448282696
        if message.chat.id == 1421340487 and message.text != '/go':
            admin_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=5)
            admin_keyboard.row(admin_key1, admin_key2)
            admin_keyboard.row(admin_key3, admin_key4)
            gg = bot.send_message(message.chat.id, 'Добро пожаловать в магазин телеграм ботов\n'
                                                   'Используйте кнопки и команды для управления ботом\n',
                                  reply_markup=admin_keyboard)
            bot.register_next_step_handler(gg, admin_panel)
        else:
            gg = bot.send_message(message.chat.id, 'Добро пожаловать в пробного бота Di Company\n'
                                                   'Бот умеет обмениваться картинками\n'
                                                   'Вы присылаете боту картинку и он вам в ответ присылает свою\n'
                                                   'Также все присланные ему картинки он добавляет себе\n'
                                                   'при ошибке напишите /go или /start',
                                  reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(gg, user_text)


def admin_panel(message):
    if message.text != '/go':
        a = message.text.lower()
        if a == 'статистика посещений':
            admin_stat_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=5)
            admin_stat_keyboard.row(admin_stat_key1, admin_stat_key2)
            admin_stat_keyboard.row(admin_stat_key3, admin_stat_key4)
            gg = bot.send_message(message.chat.id, 'Добро пожаловать в ветку статистики посещений\n'
                                                   'Используйте кнопки для управления веткой\n'
                                                   'Здесь вы можете посмотреть\n'
                                                   '-Сколько пользователей посетило бота за день/месяц\n'
                                                   '-Сколько новых пользователей за день/месяц\n'
                                                   'Для входа или возрата в меню панели админа '
                                                   'напишите /start\n'
                                                   'Для выхода из панели админа напишите /go\n',
                                  reply_markup=admin_stat_keyboard)
            bot.register_next_step_handler(gg, admin_stat)
        elif a == 'рассылка':
            gg = bot.send_message(message.chat.id,
                                  'Введите текст/фото/аудио/стикер/документ для рассылки всем пользователям\n'
                                  'Если не хотите ничего рассылать введите /start или /back',
                                  reply_markup=admin_spam_keyboard)
            bot.register_next_step_handler(gg, admin_spam)
        elif a == 'бан лист':
            bot.send_message(message.chat.id, 'Добро пожаловать в панель админа\n')
        elif a == 'редактирование фраз бота':
            bot.send_message(message.chat.id, 'Добро пожаловать в панель админа\n')
    else:
        gg = bot.send_message(message.chat.id, 'Выход из панели админа',
                              reply_markup=telebot.types.ReplyKeyboardRemove())
        start_message(message)


def admin_spam(message):
    admin_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=5)
    admin_keyboard.row(admin_key1, admin_key2)
    admin_keyboard.row(admin_key3, admin_key4)
    if message.text and message.text != '/start' and message.text != '/back' and message.text != '/go':
        TgLib.spam_to_all(bot, message.text, 0)
        gg = bot.send_message(message.chat.id, 'Рассылка прошла успешно\n'
                                               'Возврат в панель админа', reply_markup=admin_keyboard)
        start_message(message)
    elif message.photo:
        a = message.photo
        a = a[0]
        a = str(a)
        a = a[str.find(a, "'file_id'") + 12:]
        a = a[:str.find(a, "'")]
        TgLib.spam_to_all(bot, a, 1)
        gg = bot.send_message(message.chat.id, 'Рассылка прошла успешно\n'
                                               'Возврат в панель админа', reply_markup=admin_keyboard)
        start_message(message)
    elif message.audio:
        a = message.audio
        a = str(a)
        a = a[str.find(a, "'file_id'") + 12:]
        a = a[:str.find(a, "'")]
        TgLib.spam_to_all(bot, a, 2)
        gg = bot.send_message(message.chat.id, 'Рассылка прошла успешно\n'
                                               'Возврат в панель админа', reply_markup=admin_keyboard)
        start_message(message)
    elif message.sticker:
        a = message.sticker
        a = str(a)
        a = a[str.find(a, "'file_id'") + 12:]
        a = a[:str.find(a, "'")]
        TgLib.spam_to_all(bot, a, 3)
        gg = bot.send_message(message.chat.id, 'Рассылка прошла успешно\n'
                                               'Возврат в панель админа', reply_markup=admin_keyboard)
        start_message(message)
    elif message.document:
        a = message.document
        a = str(a)
        a = a[str.find(a, "'file_id'") + 12:]
        a = a[:str.find(a, "'")]
        TgLib.spam_to_all(bot, a, 4)
        gg = bot.send_message(message.chat.id, 'Рассылка прошла успешно\n'
                                               'Возврат в панель админа', reply_markup=admin_keyboard)
        start_message(message)
    elif message.voice:
        a = message.voice
        a = str(a)
        a = a[str.find(a, "'file_id'") + 12:]
        a = a[:str.find(a, "'")]
        TgLib.spam_to_all(bot, a, 5)
        gg = bot.send_message(message.chat.id, 'Рассылка прошла успешно\n'
                                               'Возврат в панель админа', reply_markup=admin_keyboard)
        start_message(message)
    elif message.text == '/start' or message.text == '/back' or message.text == '/go':
        if message.text == '/start' or message.text == '/back':
            gg = bot.send_message(message.chat.id, 'Рассылка отменена успешно\n'
                                                   'Возврат в панель админа', reply_markup=admin_keyboard)
            admin_panel(message)
        if message.text == '/go':
            gg = bot.send_message(message.chat.id, 'Выход из панели админа',
                                  reply_markup=telebot.types.ReplyKeyboardRemove())
            start_message(message)


def admin_stat(message):
    if message.text:
        a = message.text.lower()
        if a == 'новых пользователей за текущий день':
            gg = bot.send_message(message.chat.id,
                                  'Кол-во пользователей новых за сегодня : ' + str(TgLib.count_new_today()) + '\n'
                                                                                                              'Для входа или возрата в меню панели админа '
                                                                                                              'напишите /start\n'
                                                                                                              'Для выхода из панели админа напишите /go\n')
        elif a == 'пользователей за текущий день':
            gg = bot.send_message(message.chat.id,
                                  'Кол-во пользователей за сегодня : ' + str(TgLib.count_today()) + '\n'
                                                                                                    'Для входа или возрата в меню панели админа '
                                                                                                    'напишите /start\n'
                                                                                                    'Для выхода из панели админа напишите /go\n')
        elif a == 'пользователей за текущий месяц':
            gg = bot.send_message(message.chat.id,
                                  'Кол-во пользователей за месяц : ' + str(TgLib.count_month()) + '\n'
                                                                                                  'Для входа или возрата в меню панели админа '
                                                                                                  'напишите /start\n'
                                                                                                  'Для выхода из панели админа напишите /go\n')
        elif a == 'новых пользователей за текущий месяц':
            gg = bot.send_message(message.chat.id,
                                  'Кол-во новых пользователей за месяц : ' + str(TgLib.count_new_month()) + '\n'
                                                                                                            'Для входа или возрата в меню панели админа '
                                                                                                            'напишите /start\n'                                                                                             'Для выхода из панели админа напишите /go\n')
        if a == '/start' or a == '/go':
            if a == '/start':
                gg = bot.send_message(message.chat.id, 'Возврат в панель админа')
                start_message(message)
            if a == '/go':
                gg = bot.send_message(message.chat.id, 'Выход из панели админа',
                                      reply_markup=telebot.types.ReplyKeyboardRemove())
                start_message(message)
        else:
            bot.register_next_step_handler(gg, admin_stat)


def user_text(message):
    if message.photo:
        a = message.photo
        print(str(a) + "\n")
        a = a[0]
        print(a)
        a = str(a)
        a = a[str.find(a, "'file_id'") + 12:]
        a = a[:str.find(a, "'")]
        TgLib.send_random_photo(bot, a, message.chat.id)
        start_message(message)
    elif message.text == '/go':
        start_message(message)
    elif message.text == '/start':
        start_message(message)


bot.polling()

"типы входные от пользователя данных (content_types)"
# text, audio, document, photo, sticker,
# video, video_note, voice, location, contact,
# new_chat_members, left_chat_member,
# new_chat_title, new_chat_photo, delete_chat_photo,
# group_chat_created, supergroup_chat_created,
# channel_chat_created, migrate_to_chat_id,
# migrate_from_chat_id, pinned_message


"message handlers"
# content_types Типы данныз пользователя
# regexp Спец символы и тд
# commands Команды епта
# func @bot.message_handler(func=test_message, content_types=['document'])
