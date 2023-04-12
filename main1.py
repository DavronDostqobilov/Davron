from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
import os

def start(update: Update, context: CallbackContext) -> None:
    bot = context.bot
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, "Hi!")
def echo(update: Update, context: CallbackContext) -> None:
    bot = context.bot
    chat_id = update.message.chat.id
    text = update.message.text
    bot.sendMessage(chat_id, text)

