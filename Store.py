from VkObserver import Singleton


class Store(metaclass=Singleton):
    def __init__(self):
        self.__group_list = []

    def add(self, group_id):
        self.__group_list.append(group_id)

    def list(self):
        return self.__group_list
