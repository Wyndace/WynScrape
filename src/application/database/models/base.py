from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, nullable=False, unique=True,
                primary_key=True, autoincrement=True)

    def __repr__(self):
        return "<{0.__class__.__name__}(id={0.id!r})>".format(self)
