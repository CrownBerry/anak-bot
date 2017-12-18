from ChannelObserver import ChannelProvider
from VkObserver import VkProvider


def check_status(bot, job):
    status = ChannelProvider().check_status()
    if status != "None":
        bot.send_message(chat_id="@anakq_stream", text=status)


def check_vk(bot, job):
    text = VkProvider().check()
    if text != "None":
        bot.send_message(chat_id="@anakq_stream", text=text)
