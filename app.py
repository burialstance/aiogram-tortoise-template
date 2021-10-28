import logging

from aiogram import Dispatcher, executor
from loguru import logger

from loader import dp
from database import database_init, database_close
import middlewares, filters, handlers
from utils.set_bot_commands import set_default_commands
from utils.notify_admins import notify_admins


async def on_startup(dispatcher: Dispatcher):
    logger.info("on_startup...")
    await set_default_commands(dispatcher=dispatcher)
    await notify_admins(dispatcher=dispatcher, message='Startup')


async def on_shutdown(dispatcher: Dispatcher):
    logger.info("on_shutdown...")
    await database_close()



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    dp.loop.create_task(database_init(logging_level=logging.DEBUG))
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
