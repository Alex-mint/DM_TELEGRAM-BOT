import db
import logging
import os
import time
import telegram
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = '2009911477:AAE3ZP3tGYdx4OqZqWZTvyX56x1XdnqanRQ'
bot = telegram.Bot(token=TOKEN)


def start(update, context):
    time.sleep(1)
    user = update.message.from_user
    global user_id
    user_id = user.id #Id пользователя
    text1 = f'{user.first_name} напиши - “Добавить вещь”'
    text = f'Привет {user.first_name}! Я помогу тебе обменять что-то ненужное на очень нужное. Чтобы разместить вещь к обмену напиши - “Добавить вещь”. После этого тебе станут доступны вещи других пользователей. Напиши “Найти вещь” и я пришлю тебе фотографии вещей для обмена. Понравилась вещь - пиши “Обменяться”, нет - снова набирай “Найти вещь”. Если кому-то понравится предложенная тобой вещь, то я пришлю тебе контакты владельца.'
    update.message.reply_text(text)
    time.sleep(1)
    update.message.reply_text(text1)


def check_input(update, context):
    global user_name
    user_message = update.message.text
    time.sleep(1)
    if user_message == 'Добавить вещь':
        update.message.reply_text('Пожалуйста пришли мне фотографию вещи.')
    logger.info("Dietary Specification of food: %s", update.message.text)


def download_photo(update, context):
    user = update.message.from_user
    global directory
    directory = f'{user.first_name}_{user.id}'
    os.makedirs(directory, exist_ok=True)
    photo_id = update.message.photo[-1].file_id
    path = os.path.join(directory, photo_id)
    photo_file = update.message.photo[-1].get_file()
    db_path = f'{path}.jpg'  #Путь к картине
    photo_file.download(db_path)
    logger.info("Photo of %s: %s", user.first_name, 'user_photo.jpg')
    time.sleep(1)
    update.message.reply_text('Отлично))')
    time.sleep(1)
    update.message.reply_text('Пожалуйста, напиши мне название этой вещи.')



def get_title(update, context):
    global text
    text = update.message.text
    logger.info("Dietary Specification of food: %s", update.message.text)
    title = update.message.reply_text(text) #название
    update.message.reply_text('Отлично))')
    update.message.reply_text('Ваша вещь принята)')
    update.message.reply_text('Чтобы посмотреть доступные вещи напиши “Найти вещь”')


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, check_input))
    dp.add_handler(MessageHandler(Filters.photo, download_photo))
    dp.add_handler(MessageHandler(Filters.text, get_title))# не работает?

    #db.add_thing(text, directory, user_id) #в эту функцию передаются переменные из функций get_title, download_photo, check_input и создается запись в БД


    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()

# str 21, 44, 56