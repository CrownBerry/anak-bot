import logging

from telegram.ext import Updater, CommandHandler

from Config import Config
from Jobs import check_status, check_vk

if __name__ == '__main__':
    config = Config()
    updater = Updater(token=config.get_token())
    job_queue = updater.job_queue

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    job_status = job_queue.run_repeating(check_vk, interval=60, first=0)

    updater.start_polling()
