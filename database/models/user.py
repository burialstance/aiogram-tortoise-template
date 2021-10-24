from tortoise import fields

from . import AbstractBaseModel
from database.mixins import TimestampMixin


class User(AbstractBaseModel, TimestampMixin):
    telegram_id = fields.IntField(unique=True)
