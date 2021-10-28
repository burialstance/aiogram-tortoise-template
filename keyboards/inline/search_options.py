from aiogram import types
from aiogram.utils.callback_data import CallbackData
import misc.icon_characters as icons
from database.models.country import CountriesEnum
from database.types import SearchOptionsSexEnum
from misc.country_type_icons import country_type_icons
from misc.sex_type_icons import sex_type_icons

search_options_section_callback = CallbackData('search_options_section', 'section')

search_options_setup_age_callback = CallbackData('search_options_setup_age', 'from_age', 'to_age')
search_options_setup_country_callback = CallbackData('search_options_setup_country', 'country')
search_options_setup_sex_callback = CallbackData('search_options_setup_sex', 'sex')


def build_search_options_keyboard():
    kb = types.InlineKeyboardMarkup()
    kb.row(
        types.InlineKeyboardButton(text=f'{icons.underage} Возраст',
                                   callback_data=search_options_section_callback.new(section='setup_age')),
        types.InlineKeyboardButton(text=f'{icons.world} Страна',
                                   callback_data=search_options_section_callback.new(section='setup_country'))
    )
    kb.row(types.InlineKeyboardButton(text=f'{icons.couple} Пол собеседника',
                                      callback_data=search_options_section_callback.new(section='setup_sex'))
    )
    return kb


def build_setup_age_keyboard():
    kb = types.InlineKeyboardMarkup(row_width=2)
    ages = {
        'до 12 лет': {'from_age': 0, 'to_age': 12},
        '13-15 лет': {'from_age': 13, 'to_age': 15},
        '16-18 лет': {'from_age': 16, 'to_age': 18},
        '19-23 лет': {'from_age': 19, 'to_age': 23},
        '24-27 лет': {'from_age': 24, 'to_age': 27},
        '28-30+': {'from_age': 28, 'to_age': 30},
    }
    for key, value in ages.items():
        kb.insert(types.InlineKeyboardButton(text=key, callback_data=search_options_setup_age_callback.new(**value)))

    kb.row(types.InlineKeyboardButton(
        text=f'{icons.back} Назад', callback_data=search_options_section_callback.new(section='main')))
    return kb


def build_setup_country_keyboard():
    kb = types.InlineKeyboardMarkup(row_width=2)
    for country in CountriesEnum:
        flag = country_type_icons.get(country, country_type_icons[CountriesEnum.ALL])
        kb.insert(types.InlineKeyboardButton(
            text=f"{flag} {country.value}",
            callback_data=search_options_setup_country_callback.new(country=country.value))
        )

    kb.row(types.InlineKeyboardButton(
        text=f'{icons.back} Назад', callback_data=search_options_section_callback.new(section='main')))
    return kb


def build_setup_sex_keyboard():
    kb = types.InlineKeyboardMarkup(row_width=2)

    for sex in SearchOptionsSexEnum:
        icon = sex_type_icons[sex]
        kb.insert(types.InlineKeyboardButton(
            text=f'{icon} {sex.value}',
            callback_data=search_options_setup_sex_callback.new(sex=sex.value))
        )

    kb.row(types.InlineKeyboardButton(
        text=f'{icons.back} Назад', callback_data=search_options_section_callback.new(section='main')))
    return kb
