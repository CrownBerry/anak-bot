from ChannelObserver import ChannelProvider


def check_status(bot, job):
    status = ChannelProvider().check_status()
    if status != "None":
        bot.send_message(chat_id="@anakq_stream", text=status)


def check_vk(bot, job):
    text = ChannelProvider().check_status()
    if text != "None":
        bot.send_message(chat_id="@anakq_stream", text=text)
