from inventree_uah_exchange.rates import convert, parse_nbu

NBU = [
    {'cc': 'USD', 'rate': 40.0},
    {'cc': 'EUR', 'rate': 44.0},
    {'cc': 'JPY', 'rate': 0.25},
]


def test_usd_base():
    rates = convert(parse_nbu(NBU), 'USD', ['UAH', 'EUR', 'JPY', 'USD'])
    assert rates['USD'] == 1.0
    assert rates['UAH'] == 40.0
    assert abs(rates['EUR'] - 40 / 44) < 1e-12
    assert rates['JPY'] == 160.0


def test_uah_base():
    rates = convert(parse_nbu(NBU), 'UAH', ['USD', 'EUR'])
    assert rates == {'UAH': 1.0, 'USD': 1 / 40, 'EUR': 1 / 44}


def test_unknown_symbol_skipped():
    assert 'XYZ' not in convert(parse_nbu(NBU), 'USD', ['XYZ', 'EUR'])


def test_unknown_base():
    assert convert(parse_nbu(NBU), 'XYZ', ['USD']) == {}
