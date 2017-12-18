import configparser


class Config:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        default_config = config['DEFAULT']
        self.__telegram_token = default_config.get('tgToken')
        self.__twitch_client_id = default_config.get('twitchClientId')
        self.__oauth_token = default_config.get('oauthToken')
        self.__channel_id = default_config.get('channelId')
        self.__vk_token = default_config.get('vkToken')
        self.__group = default_config.get('group')

    def get_token(self):
        return self.__telegram_token

    def get_client_id(self):
        return self.__twitch_client_id

    def get_oauth_token(self):
        return self.__oauth_token

    def get_channel(self):
        return self.__channel_id

    def get_vk_token(self):
        return self.__vk_token

    def get_group(self):
        return self.__group
