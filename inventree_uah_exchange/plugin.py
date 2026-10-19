"""Exchange rates from the National Bank of Ukraine (bank.gov.ua), which include UAH."""

import requests
import structlog

from plugin import InvenTreePlugin
from plugin.mixins import CurrencyExchangeMixin

from . import PLUGIN_VERSION
from .rates import convert, parse_nbu

logger = structlog.get_logger('inventree')

NBU_URL = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'


class UAHExchangePlugin(CurrencyExchangeMixin, InvenTreePlugin):
    """Currency exchange rates from the NBU official daily rates."""

    NAME = 'UAHExchange'
    SLUG = 'uahexchange'
    TITLE = 'UAH Exchange (NBU)'
    DESCRIPTION = 'Exchange rates from the National Bank of Ukraine, including UAH'
    AUTHOR = 'Yehor'
    VERSION = PLUGIN_VERSION
    WEBSITE = 'https://github.com/Bravo13/inventree-uah-exchange'
    LICENSE = 'MIT'

    def update_exchange_rates(self, base_currency: str, symbols: list[str]) -> dict:
        """Fetch today's NBU rates and convert them to the base currency."""
        response = requests.get(NBU_URL, timeout=30)
        if response.status_code != 200:
            logger.warning('NBU exchange rates: server returned status %s', response.status_code)
            return {}

        uah_per = parse_nbu(response.json())
        rates = convert(uah_per, base_currency, symbols)
        if not rates:
            logger.warning('NBU exchange rates: base currency %s not published', base_currency)
            return {}

        missing = sorted({s.upper() for s in symbols} - set(rates))
        if missing:
            logger.warning('NBU exchange rates: no rate for %s', ', '.join(missing))
        return rates
