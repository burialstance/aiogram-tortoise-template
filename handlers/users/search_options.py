from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, CommandSettings, Text
from aiogram.types import ParseMode

from loader import dp
from database.models.user import User
from middlewares.userdata import userdata_required
from database.services import UserService
from middlewares.throttling import rate_limit
from misc.messages import build_search_options_text
from keyboards.inline.search_options import (
    build_search_options_keyboard, search_options_section_callback,
    build_setup_age_keyboard, search_options_setup_age_callback,
    build_setup_country_keyboard, search_options_setup_country_callback,
    build_setup_sex_keyboard, search_options_setup_sex_callback
)


async def show_search_options(message: types.Message, user: User, edit_message=False):
    answer, parse_mode = await build_search_options_text(user)
    keyboard = build_search_options_keyboard()
    if edit_message:
        return await message.edit_text(text=answer, parse_mode=parse_mode, reply_markup=keyboard)
    return await message.answer(answer, parse_mode=parse_mode, reply_markup=keyboard)


@rate_limit(limit=1)
@userdata_required
@dp.message_handler(Text(equals=['/search_options']))
async def process_show_search_options(message: types.Message, user: User):
    await show_search_options(message=message, user=user, edit_message=False)


@dp.callback_query_handler(search_options_section_callback.filter())
async def process_sections_callback(call: types.CallbackQuery, callback_data: dict):
    section = callback_data.get('section')
    keyboards_sections = {
        'main': build_search_options_keyboard,

        'setup_age': build_setup_age_keyboard,
        'setup_country': build_setup_country_keyboard,
        'setup_sex': build_setup_sex_keyboard
    }

    keyboard = keyboards_sections.get(section)()
    await call.message.edit_reply_markup(reply_markup=keyboard)
    await call.answer()


# SETUP AGE
@userdata_required
@dp.callback_query_handler(search_options_setup_age_callback.filter())
async def process_setup_age_callback(call: types.CallbackQuery, callback_data: dict, user: User):
    from_age = callback_data.get('from_age')
    to_age = callback_data.get('to_age')
    user = await UserService.search_options.setup_age(user=user, from_age=from_age, to_age=to_age)
    await show_search_options(call.message, user=user, edit_message=True)
    await call.answer(text=f'Изменено на {user.search_options.from_age}-{user.search_options.to_age}')


# SETUP COUNTRY
@userdata_required
@dp.callback_query_handler(search_options_setup_country_callback.filter())
async def process_setup_country_callback(call: types.CallbackQuery, callback_data: dict, user: User):
    country = callback_data.get('country')
    user = await UserService.search_options.setup_country(user=user, country=country)
    await show_search_options(call.message, user, edit_message=True)
    await call.answer(f'Изменено на: {user.search_options.country.name.value}')


# SETUP SEX
@userdata_required
@dp.callback_query_handler(search_options_setup_sex_callback.filter())
async def process_setup_sex_callback(call: types.CallbackQuery, callback_data: dict, user: User):
    sex = callback_data.get('sex')
    user = await UserService.search_options.setup_sex(user=user, sex=sex)
    await show_search_options(message=call.message, user=user, edit_message=True)
    await call.answer(f'Изменено на: {user.sex}')
