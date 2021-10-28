import sys

from tortoise import Tortoise
from loguru import logger
import logging


from . import settings
from . import signals


async def database_init(logging_level=None):
    if logging_level:
        logging.getLogger("db_client").setLevel(logging_level)
    await Tortoise.init(settings.DATABASE_CONFIG)
    await Tortoise.generate_schemas()
    logger.info("Tortoise inited!")


async def database_close():
    await Tortoise.close_connections()
    logger.info("Tortoise closed!")

