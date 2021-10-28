from database.models.country import CountriesEnum
import misc.icon_characters as icons

country_type_icons = {
    CountriesEnum.RUSSIA: icons.russia_flag,
    CountriesEnum.UKRAINE: icons.ukraine_flag,
    CountriesEnum.BELARUS: icons.belarus_flag,
    CountriesEnum.KAZAKHSTAN: icons.kazakhstan_flag,
    CountriesEnum.UZBEKISTAN: icons.uzbekistan_flag,
    CountriesEnum.TAJIKISTAN: icons.tajikistan_flag,
    CountriesEnum.TURKMENISTAN: icons.turkmenistan_flag,
    CountriesEnum.AZERBAIJAN: icons.azerbaijan_flag,
    CountriesEnum.ARMENIA: icons.armenia_flag,
    CountriesEnum.MOLDOVA: icons.moldova_flag,
    CountriesEnum.ALL: icons.world
}