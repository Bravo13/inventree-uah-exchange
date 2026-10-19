"""Convert NBU official rates (UAH per unit) to rates relative to a base currency."""

UAH = 'UAH'


def parse_nbu(data: list[dict]) -> dict[str, float]:
    """Return {currency: UAH per 1 unit} from the NBU JSON response, plus UAH itself."""
    uah_per = {UAH: 1.0}
    for row in data:
        code, rate = row.get('cc'), row.get('rate')
        if code and rate:
            uah_per[code.upper()] = float(rate)
    return uah_per


def convert(uah_per: dict[str, float], base_currency: str, symbols: list[str]) -> dict[str, float]:
    """Return {symbol: units of symbol per 1 base_currency}, as InvenTree expects.

    Symbols the NBU doesn't publish are left out. Returns {} if the base itself is unknown.
    """
    base = base_currency.upper()
    if base not in uah_per:
        return {}
    rates = {base: 1.0}
    for symbol in symbols:
        code = symbol.upper()
        if code in uah_per:
            rates[code] = uah_per[base] / uah_per[code]
    return rates
