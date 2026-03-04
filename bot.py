import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 Welcome to ViralTube AI Bot!\nSend topic to get script idea.")

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(message, f"🔥 Script Idea for: {message.text}\n\nHook: This will shock you!\nContent: Explain topic in 5 points.\nCTA: Subscribe for more!")

bot.polling()
