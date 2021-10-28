from typing import Type, List, Optional

from tortoise import BaseDBAsyncClient
from tortoise.signals import pre_save, post_save
from loguru import logger
from database.models.user import User
from database.models.search_options import SearchOptions
from database.models.country import Country, CountriesEnum


@pre_save(User)
async def signal_create_search_options_for_user(sender: "Type[User]", instance: User, using_db, update_fields) -> None:
    if not await instance.search_options:
        instance.search_options = await SearchOptions.create()
        logger.info(f'for {instance}: created default {instance.search_options}')

    if not await instance.country:
        instance.country, _ = await Country.get_or_create(name=CountriesEnum.RUSSIA)
        logger.info(f'for {instance}: created default {instance.country}')


@pre_save(SearchOptions)
async def signal_create_search_options_country(sender: "Type[SearchOptions]", instance: SearchOptions, using_db, update_fields) -> None:
    if not await instance.country:
        instance.country, _ = await Country.get_or_create(name=CountriesEnum.RUSSIA)
        logger.info(f'for {instance}: created default {instance.country}')
