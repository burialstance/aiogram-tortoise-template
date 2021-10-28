from enum import Enum


class SexEnum(Enum):
    MALE = 'мужской'
    FEMALE = 'женский'


class UserSexEnum(Enum):
    MALE = 'мужской'
    FEMALE = 'женский'
    UNKNOWN = 'неизвестный'


class SearchOptionsSexEnum(Enum):
    MALE = 'мужской'
    FEMALE = 'женский'
    ALL = 'все'


class CountriesEnum(Enum):
    RUSSIA = 'Россия'
    UKRAINE = 'Украина'
    BELARUS = 'Беларусь'
    KAZAKHSTAN = 'Казахстан'
    UZBEKISTAN = 'Узбекистан'
    TAJIKISTAN = 'Таджикистан'
    TURKMENISTAN = 'Туркменистан'
    AZERBAIJAN = 'Азербайджан'
    ARMENIA = 'Армения'
    MOLDOVA = 'Молдова'
    ALL = 'Все'
