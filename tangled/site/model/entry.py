from sqlalchemy.schema import Column
from sqlalchemy.types import String, Text

from .base import Base, BaseMixin, TimestampMixin


class Entry(Base, BaseMixin, TimestampMixin):

    slug = Column(String(length=100), nullable=False, unique=True)
    title = Column(String(length=100), nullable=False)
    content = Column(Text, nullable=False)
