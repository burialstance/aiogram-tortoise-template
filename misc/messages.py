from typing import Union, Optional

from aiogram.types import ParseMode
from aiogram.utils.markdown import bold, text
import misc.icon_characters as icons
from misc.sex_type_icons import sex_type_icons
from misc.country_type_icons import country_type_icons
from database.models.user import User

START_COMMAND_TEXT = """
start command text
user: {user}
"""


async def build_search_options_text(user):
    await user.fetch_related('search_options', 'search_options__country')
    search_from_age = user.search_options.from_age
    search_to_age = user.search_options.to_age
    search_sex = user.search_options.sex.value
    search_country = user.search_options.country.name.value
    search_country_icon = country_type_icons[user.search_options.country.name]

    message = f"""{icons.settings}<b>Опции поиска собеседника</b>
    Возраст: {search_from_age}-{search_to_age}
    Страна: {search_country_icon} {search_country}
    Пол: {search_sex}    
    """

    return message, ParseMode.HTML


async def build_user_profile_text(user: User):
    await user.fetch_related('country', 'search_options', 'search_options__country')
    telegram_id = user.telegram_id
    user_sex = user.sex.value
    print(type(user.sex), user.sex)
    icon_user_sex = sex_type_icons[user.sex]
    user_age = user.age
    user_country = user.country.name.value
    print(type(user.country.name), user.country.name)

    icon_user_country = country_type_icons[user.country.name]

    message = f"""
{icons.person} <b>Профиль</b><code> {telegram_id}</code>
    Ваш пол: {icon_user_sex} {user_sex}
    Ваш возраст: {user_age}
    Ваша страна: {icon_user_country} {user_country}
"""

    return message, ParseMode.HTML