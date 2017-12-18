import vk

from Config import Config


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class VkProvider(metaclass=Singleton):
    def __init__(self):
        self.__config = Config()
        self.__vk = VkService(self.__config)
        self.__last_id = self.__vk.get_last_post()['id']

    def check(self):
        old_id = self.__last_id
        new_post = self.__vk.get_last_post()
        if old_id == new_post['id']:
            return 'None'
        return new_post['text']


class VkService:
    def __init__(self, config):
        self.__token = config.get_vk_token()
        self.__group = config.get_group()
        self.__api = vk.API(vk.Session(access_token=self.__token))

    def get_last_post(self):
        return self.__api.wall.get(owner_id=-self.__group, count=1, filter='owner')[1]
