from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ParseMode

from loader import dp

from database.models.user import User
from middlewares.userdata import userdata_required
from middlewares.throttling import rate_limit
from misc.messages import START_COMMAND_TEXT


@userdata_required
@dp.message_handler(CommandStart())
async def process_start_command(message: types.Message, user: User):
    await message.answer(
        START_COMMAND_TEXT.format(user=user.telegram_id),
        parse_mode=ParseMode.MARKDOWN)

