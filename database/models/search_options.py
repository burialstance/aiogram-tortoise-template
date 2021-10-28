import enum
from tortoise import fields

from database.mixins import TimestampMixin
from database.models import AbstractBaseModel
from database.types import SearchOptionsSexEnum


class SearchOptions(AbstractBaseModel, TimestampMixin):
    user: fields.OneToOneRelation['User']

    sex: SearchOptionsSexEnum = fields.CharEnumField(enum_type=SearchOptionsSexEnum, default=SearchOptionsSexEnum.ALL)
    from_age: int = fields.IntField(null=True)
    to_age: int = fields.IntField(null=True)

    country = fields.ForeignKeyField(
        'models.Country', related_name='search_options', on_delete=fields.CASCADE)
