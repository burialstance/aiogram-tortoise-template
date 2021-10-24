from aiogram.dispatcher.handler import current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from database.models.user import User


def userdata_required(func):
    """Setting login_required to function"""
    setattr(func, 'userdata_required', True)
    return func


class UserMiddleware(BaseMiddleware):

    def __init__(self):
        super(UserMiddleware, self).__init__()

    async def push_user_to_context(self, telegram_id: int, data: dict):
        handler = current_handler.get()
        if handler and getattr(handler, 'userdata_required', False):
            user, created = await User.get_or_create(telegram_id=telegram_id)
            data['user'] = user

    async def on_process_message(self, message: Message, data: dict):
        await self.push_user_to_context(telegram_id=message.from_user.id, data=data)

    async def on_process_callback_query(self, callback_query: CallbackQuery, data: dict):
        await self.push_user_to_context(telegram_id=callback_query.message.from_user.id, data=data)
