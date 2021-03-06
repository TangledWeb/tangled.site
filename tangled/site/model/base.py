from datetime import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import DateTime, Integer

from sqlalchemy.ext.declarative import declarative_base, declared_attr


Base = declarative_base()


class BaseMixin:

    id = Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def __json_data__(self):
        data = {}
        for c in self.__table__.columns:
            data[c.name] = getattr(self, c.name)
        return data


class TimestampMixin:

    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)
