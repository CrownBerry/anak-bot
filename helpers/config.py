import configparser
import os


class Config:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        if config.has_section('DEFAULT'):
            default_config = config['DEFAULT']
            self.__telegram_token = default_config.get('tgToken')
            self.__vk_token = default_config.get('vkToken')
            self.__group = default_config.get('group')
            self.__connection_string = default_config.get('connectionString')
        else:
            self.__telegram_token = os.environ['TG_TOKEN']
            self.__vk_token = os.environ['VK_TOKEN']
            self.__group = os.environ['GROUP']
            self.__connection_string = os.environ['CONNECTION_STRING']

    def get_token(self):
        return self.__telegram_token

    def get_vk_token(self):
        return self.__vk_token

    def get_group(self):
        return self.__group

    def connection_string(self):
        return self.__connection_string
