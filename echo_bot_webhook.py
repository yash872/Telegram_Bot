import logging
from flask import Flask, request
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
from telegram import Bot, Update

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "1280107757:AAFyERAqLxyk03L3uOTPga57H1eiVSQAX38"

app  = Flask(__name__)

@app.route('/')
def index():
	return "Hey! It's Me YashBot"

@app.route(f'/{TOKEN}',methods=['GET', 'POST'])
def webhook():
	update = Update.de_json(request.get_json(), bot)
	dp.process_update(update)
	return "ok"


def start(bot,update):
	print(update)
	author = update.message.from_user.first_name
	reply = "Hi! {}".format(author)
	bot.send_message(chat_id=update.message.chat_id, text=reply)

def _help(bot,update):
	help_text='Hey! This is my Help Text :) '
	bot.send_message(chat_id=update.message.chat_id, text=help_text)

def echo_text(bot,update):
	echo_text=update.message.text
	bot.send_message(chat_id=update.message.chat_id, text=echo_text)

def echo_sticker(bot,update):
	sticker=update.message.sticker.file_id
	bot.send_sticker(chat_id=update.message.chat_id, sticker=sticker)

def error(bot,update):
	logger.error("Update '%s' caused error '%s'",update, update.error)


if __name__ == '__main__':
	bot = Bot(TOKEN)
	bot.set_webhook("https://053462e87ec4.ngrok.io/" + TOKEN)
	dp = Dispatcher(bot, None)
	dp.add_handler(CommandHandler("start",start))
	dp.add_handler(CommandHandler("help",_help))
	dp.add_handler(MessageHandler(Filters.text,echo_text))
	dp.add_handler(MessageHandler(Filters.sticker,echo_sticker))
	dp.add_error_handler(error)
	logger.info("Webhook Started . . . . . .  ")
	app.run(port=8443)
