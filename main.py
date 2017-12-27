import logging

from telegram.ext import Updater, CommandHandler

from helpers.config import Config
from helpers.jobs import check_vk, notify

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    config = Config()
    updater = Updater(token=config.get_token())
    job_queue = updater.job_queue
    dispatcher = updater.dispatcher

    notify_handler = CommandHandler('notify_me', notify)

    job_status = job_queue.run_repeating(check_vk, interval=60, first=0)
    dispatcher.add_handler(notify_handler)

    updater.start_polling()
