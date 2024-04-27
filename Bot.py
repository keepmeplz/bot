import telebot
from telebot import types

bot = telebot.TeleBot('7117322157:AAES5f0x_z5lwlGYLWEs3yCg8z3LZT4euFQ')

# Создаем клавиатуры
kurator = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
kurator_table = types.KeyboardButton("вызываю куратора!!")
question_table = types.KeyboardButton("Задать вопрос")
kurator.add(kurator_table, question_table)

# Feedback
say = types.InlineKeyboardMarkup()
say_yes = types.InlineKeyboardButton("Да", callback_data="Yes")
say_no = types.InlineKeyboardButton("Нет", callback_data="No")
say.add(say_yes, say_no)

def start_message(message):
    bot.send_message(message.chat.id, "Путник! С какой целью ты пробудил Партурнакса?",reply_markup=kurator)

def call_curator(message):
    bot.send_message(message.chat.id, "Куратор вызван!")

@bot.message_handler(commands=['start'])
def handle_start(message):
    start_message(message)

@bot.message_handler(func=lambda message: message.text == "Задать вопрос")
def ask_question(message):
    bot.send_message(message.chat.id, "Слушаю тебя. Введите ваш вопрос:")
    bot.register_next_step_handler(message, process_question)

def process_question(message):
    print (message)
    question = message.text
# Отправляем вопрос на обработку в модель машинного обучения в другом файле
    answer = "хуй" # asyncio.run(process_message(question))
    bot.send_message(message.chat.id, answer)



# Спросим пользователя, понравился ли ответ
    bot.send_message(message.chat.id, "Понравился ли вам ответ?", reply_markup=say)

@bot.callback_query_handler(func=lambda call: call.data == "Yes")
def handle_yes(call):
    bot.send_message(call.message.chat.id, "Всегда рад помочь. Обращайтесь)")

@bot.callback_query_handler(func=lambda call: call.data == "No")
def handle_no(call):
    call_curator(call.message)

@bot.message_handler(func=lambda message: message.text == "начнем с начала!!")
def handle_reset(message):
    start_message(message)

@bot.message_handler(func=lambda message: message.text == "вызываю куратора!!")
def handle_curator(message):
    call_curator(message)

@bot.message_handler(func=lambda message: True)
def handle_communication(message):
    bot.send_message(message.chat.id, "Реализация бота для общения...")

bot.polling()