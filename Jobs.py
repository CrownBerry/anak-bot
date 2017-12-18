from ChannelObserver import ChannelProvider


def check_status(bot, job):
    status = ChannelProvider().check_status()
    if status != "None":
        bot.send_message(chat_id="@anakq_stream", text=status)
