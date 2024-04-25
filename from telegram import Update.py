import telegram.ext
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = '6553053895:AAGass2qrX318VeYL7T9Gz79SyWLQ4QKpq4'

updates_history = []

def start(update: Update, context: CallbackContext):
    update.message.reply_text("hellow")

def show_updates(update: Update, context: CallbackContext):
    if updates_history:
        update.message.reply_text('\n'.join(updates_history))
    else:
        update.message.reply_text("История обновлений пуста.")

def process_text(update: Update, context: CallbackContext):
    text = update.message.text
    updates_history.append(text)
    update.message.reply_text(text)

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("updates", show_updates))
    
    # Добавляем обработчик для текстовых сообщений от пользователя, указывая функцию process_text и передавая context
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, process_text, context=CallbackContext))

    updater.start_polling()
    updater.idle()

main()
