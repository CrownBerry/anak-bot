from ChannelObserver import ChannelProvider
from Store import Store
from VkObserver import VkProvider


def check_status(bot, job):
    status = ChannelProvider().check_status()
    if status != "None":
        bot.send_message(chat_id="@anakq_stream", text=status)


def check_vk(bot, job):
    text = VkProvider().check()
    if text != "None":
        url = VkProvider().is_photo()
        for group in Store().list():
            bot.send_message(chat_id=group, text=text)
            if url is not None:
                bot.send_photo(chat_id=group, photo=url)
