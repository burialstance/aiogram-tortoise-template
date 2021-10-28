from tortoise import fields

from database.models import AbstractBaseModel
from database.mixins import TimestampMixin
from database.types import CountriesEnum


class Country(AbstractBaseModel, TimestampMixin):
    name: CountriesEnum = fields.CharEnumField(enum_type=CountriesEnum, default=CountriesEnum.RUSSIA)
    search_options: fields.ForeignKeyRelation['SearchOptions']
