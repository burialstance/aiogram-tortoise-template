from aiogram import types
from aiogram.utils.callback_data import CallbackData

from database.types import UserSexEnum, CountriesEnum
import misc.icon_characters as icons
from misc.country_type_icons import country_type_icons
from misc.sex_type_icons import sex_type_icons

user_profile_section_callback = CallbackData('user_profile', 'section')
user_profile_setup_country_callback = CallbackData('user_profile_setup_country', 'country')
user_profile_setup_sex_callback = CallbackData('user_profile_setup_sex', 'sex')


def build_user_profile_keyboard():
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton(text=f'{icons.underage} Изменить Возраст',
                                   callback_data=user_profile_section_callback.new(section='setup_age')),
        types.InlineKeyboardButton(text=f'{icons.world} Изменить страну',
                                   callback_data=user_profile_section_callback.new(section='setup_country')),
        types.InlineKeyboardButton(text=f'{icons.couple} Изменить Пол',
                                   callback_data=user_profile_section_callback.new(section='setup_sex'))
    )

    return kb


def build_user_profile_setup_country_keyboard():
    kb = types.InlineKeyboardMarkup(row_width=2)
    for country in CountriesEnum:
        if country == CountriesEnum.ALL:
            continue
        country_icon = country_type_icons.get(country, country_type_icons[CountriesEnum.ALL])
        kb.insert(types.InlineKeyboardButton(
            text=f"{country_icon} {country.value}",
            callback_data=user_profile_setup_country_callback.new(country=country.value))
        )

    kb.row(types.InlineKeyboardButton(
        text=f'{icons.back} Назад', callback_data=user_profile_section_callback.new(section='main')))
    return kb


def build_user_profile_setup_sex_keyboard():
    kb = types.InlineKeyboardMarkup(row_width=2)
    for sex in UserSexEnum:
        if sex == UserSexEnum.UNKNOWN:
            continue
        sex_icon = sex_type_icons[sex]
        kb.insert(types.InlineKeyboardButton(
            text=f"{sex_icon} {sex.value}",
            callback_data=user_profile_setup_sex_callback.new(sex=sex.value))
        )
    kb.row(types.InlineKeyboardButton(
        text=f'{icons.back} Назад', callback_data=user_profile_section_callback.new(section='main')))
    return kb
