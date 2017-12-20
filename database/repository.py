from sqlalchemy import create_engine

from database.models import ses_scope, Group, Base
from helpers.config import Config
from helpers.vk_observer import Singleton


class MainRepository(metaclass=Singleton):
    def __init__(self):
        self.__config = Config()
        self.__engine = create_engine(self.__config.connection_string(), echo=True)
        Base.metadata.create_all(self.__engine)

    def add_group(self, input_group_id):
        with ses_scope(self.__engine) as ses:
            instance = ses.query(Group).filter(Group.group_id == input_group_id).first()
            if instance:
                return "You are already subscribed"
            else:
                group = Group(group_id=input_group_id)
                ses.add(group)
                return "Subscribe this group to notify list"

    def get_group(self):
        with ses_scope(self.__engine) as ses:
            result = ses.query(Group).all()
            return [group.group_id for group in result]
