from twitch import TwitchClient

from Config import Config


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ChannelProvider(metaclass=Singleton):
    def __init__(self):
        self._config = Config()
        self.__channelObserver = ChannelObserver(self._config)
        self.__status = None

    def check_status(self):
        response = "None"
        old_status = self.__status
        new_status = self.__channelObserver.stream_status()
        if old_status == new_status:
            response = "None"
        elif old_status is None:
            response = "Go online:\r\n "
            response += self.__channelObserver.stream_title()
        elif new_status is None:
            response = "Go offline"
        self.__status = new_status
        return response


class ChannelObserver:
    def __init__(self, config):
        self.__channel_id = config.get_channel()
        self.__client = TwitchClient(client_id=config.get_client_id(), oauth_token=config.get_oauth_token())

    def stream_status(self):
        return self.__client.streams.get_stream_by_user(self.__channel_id)

    def stream_title(self):
        return self.__client.channels.get_by_id(self.__channel_id).status
