import telebot
import os
from telebot import types

bot = telebot.TeleBot('7117322157:AAES5f0x_z5lwlGYLWEs3yCg8z3LZT4euFQ')



# Папка для хранения фотографий
PHOTO_FOLDER = 'photos'
if not os.path.exists(PHOTO_FOLDER):
    os.makedirs(PHOTO_FOLDER)
# Множество для отслеживания уже сохраненных фотографий
saved_photos = set()
# Feedback
say = types.InlineKeyboardMarkup()
say_yes = types.InlineKeyboardButton("Да", callback_data="Yes")
say_no = types.InlineKeyboardButton("Нет", callback_data="No")
say.add(say_yes, say_no)

# Начальное сообщение
def start_message(message):
    bot.send_message(message.chat.id, "Путник! С какой целью ты пробудил Партурнакса?")

@bot.message_handler(commands=['start'])
def handle_start(message):
    start_message(message)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    for photo in message.photo:
        photo = message.photo[-1]  # сохраняем последнюю (наибольшую по размеру) фотографию

        if photo.file_id not in saved_photos:  # Проверяем, не сохраняли ли уже эту фотографию
            file_info = bot.get_file(photo.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            file_name = os.path.join(PHOTO_FOLDER, f"{photo.file_id}.jpg")
            with open(file_name, 'wb') as new_file:
                new_file.write(downloaded_file)
            saved_photos.add(photo.file_id)  # Добавляем идентификатор в множество сохраненных фотографий
    bot.reply_to(message, 'Фотографии сохранены.')


@bot.message_handler(content_types=['document'])
def handle_file(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    save_path = 'file' + message.document.file_name  # сохраняем файл с его исходным именем
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, 'Файл сохранен.')

@bot.message_handler(commands=['хуй'])
def process_question(message):
    # Отправка фотографии через бота
    photo_path = "C:/Users/Nikita/Downloads" 
     # Замените на корректный путь к фотографии
    for filename in os.listdir(photo_path):
        file_path = os.path.join(photo_path, filename)
        with open(file_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, "Все фотографии отправлены.")
    # Спросим пользователя, понравился ли ответ
    bot.send_message(message.chat.id, "Понравился ли вам ответ?", reply_markup=say)

@bot.callback_query_handler(func=lambda call: call.data == "Yes")
def handle_yes(call):
    bot.send_message(call.message.chat.id, "Всегда рад помочь. Обращайтесь)")

@bot.callback_query_handler(func=lambda call: call.data == "No")
def handle_no(call):
    bot.send_message(call.message.chat.id, "Жаль, что вам не понравилось.")

@bot.message_handler(func=lambda message: True)
def handle_communication(message):
    bot.send_message(message.chat.id, "Реализация бота для общения...")

bot.polling(none_stop=True)
