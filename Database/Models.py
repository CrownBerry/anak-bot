from contextlib import contextmanager

import sys
from sqlalchemy import Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()
metadata = Base.metadata

@contextmanager
def ses_scope(engine):
    """Provide a transactional scope around a series of operations."""
    session = Session(engine)
    try:
        yield session
        session.commit()
    except:
        error = str(sys.exc_info())
        print("Error is: ", error)
        session.rollback()
        raise
    finally:
        session.close()


class Group(Base):
    __tablename__ = "groups"
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer)
