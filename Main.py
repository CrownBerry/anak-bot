import logging

from telegram.ext import Updater, CommandHandler

from Config import Config
from Jobs import check_status, check_vk
from Store import Store


def notify(bot, update):
    Store().add(update.message.chat_id)
    bot.send_message(chat_id=update.message.chat_id,
                     text="Added this group to notify list")

if __name__ == '__main__':
    config = Config()
    updater = Updater(token=config.get_token())
    job_queue = updater.job_queue
    dispatcher = updater.dispatcher

    notify_handler = CommandHandler('notify_me', notify)

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    job_status = job_queue.run_repeating(check_vk, interval=60, first=0)
    dispatcher.add_handler(notify_handler)

    updater.start_polling()
