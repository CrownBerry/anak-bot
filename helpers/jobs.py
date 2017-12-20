from database.repository import MainRepository
from helpers.vk_observer import VkProvider


def notify(bot, update):
    result = MainRepository().add_group(update.message.chat_id)
    bot.send_message(chat_id=update.message.chat_id,
                     text=result)


def check_vk(bot, job):
    text = VkProvider().check()
    text = text.replace("<br>", "\n")
    if text != "None":
        url = VkProvider().is_photo()
        group_list = MainRepository().get_group()
        for group in group_list:
            bot.send_message(chat_id=group, text=text)
            if url is not None:
                bot.send_photo(chat_id=group, photo=url)
