from typing import Optional, Union

from database.models.user import User
from database.models.search_options import SearchOptions
from database.models.country import Country
from database.types import UserSexEnum, SearchOptionsSexEnum, CountriesEnum


async def get_user(user: Union[User, int], *fetch_related) -> User:
    if not any([isinstance(user, User), isinstance(user, int)]):
        raise ValueError(f'value "user" must be int or <User> instance')

    if isinstance(user, int) or isinstance(user, str) and user.isdigit():
        telegram_id = user
        user, _ = await User.get_or_create(telegram_id=telegram_id)
    if fetch_related:
        await user.fetch_related(*fetch_related)
    return user


class UserSearchOptionsService:
    @staticmethod
    async def setup_age(user: Union[User, int], from_age: int, to_age: int) -> User:
        user = await get_user(user, 'search_options')
        user.search_options.from_age, user.search_options.to_age = int(from_age), int(to_age)
        await user.search_options.save(update_fields=['from_age', 'to_age'])
        return user

    @staticmethod
    async def setup_sex(user: Union[User, int], sex: SearchOptionsSexEnum) -> User:
        user = await get_user(user, 'search_options')
        if not isinstance(sex, SearchOptionsSexEnum):
            sex = SearchOptionsSexEnum(sex)
        user.search_options.sex = sex
        await user.search_options.save(update_fields=['sex'])
        return user

    @staticmethod
    async def setup_country(user: Union[User, int], country: CountriesEnum) -> User:
        user = await get_user(user, 'search_options__country')
        if not isinstance(country, CountriesEnum):
            country = CountriesEnum(country)
        user.search_options.country, _ = await Country.get_or_create(name=country)
        await user.search_options.save()
        return user


class UserService:
    search_options = UserSearchOptionsService

    @staticmethod
    async def setup_age(user: Union[User, int], age: int) -> User:
        if not isinstance(age, int):
            age = int(age)
        user = await get_user(user)
        user.age = age
        await user.save()
        return user

    @staticmethod
    async def setup_sex(user: Union[User, int], sex: UserSexEnum) -> User:
        if not isinstance(sex, UserSexEnum):
            sex = UserSexEnum(sex)
        user = await get_user(user)
        user.sex = sex
        await user.save()
        return user

    @staticmethod
    async def setup_country(user: Union[User, int], country: CountriesEnum) -> User:
        if not isinstance(country, CountriesEnum):
            country = CountriesEnum(country)
        user = await get_user(user)
        user.country, _ = await Country.get_or_create(name=country)
        await user.save()
        return user