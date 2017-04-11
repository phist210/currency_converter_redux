from currency import Currency, DifferentCurrencyCodeError
from currency_converter import CurrencyConverter

from nose.tools import raises


@raises(DifferentCurrencyCodeError)
def test_different_currency_code_error():
    Currency(5, "USD") + Currency(5, "JPY")


@raises(DifferentCurrencyCodeError)
def test_different_currency_code_error():
    Currency(5, "GBP") - Currency(5, "EUR")


@raises(DifferentCurrencyCodeError)
def test_different_currency_code_error():
    Currency(5, "USD") * Currency(5, "JPY")


def test_are_ne():
    assert Currency(5, "USD") != Currency(5, "JPY")


def test_are_eq_same_style():
    assert Currency(5, "EUR") == Currency(5, "EUR") #== True
    assert Currency(5, "£") == Currency(5, "£") # == True


def test_are_eq_diff_style():
    assert Currency(5, "JPY") == Currency('¥5')


def test_add_instances():
    assert Currency(15, "USD") + Currency(5, "USD") == Currency('$20')


def test_sub_instances():
    assert Currency(5, "USD") - Currency(15, "USD") == Currency('$-10')


def test_mul_():
    assert Currency(5, "USD") * 5 == Currency(25, 'USD')


def test_rmul_():
    assert 5 * Currency(5, "USD") == Currency(25, 'USD')


def test_conversion():
    c = CurrencyConverter()
    assert c.convert(Currency(1, "USD"), "USD") == Currency(1, "USD")
    assert c.convert(Currency(1, "USD"), "EUR") == Currency(0.74, "EUR")
    assert c.convert(Currency(1, "EUR"), "USD") != Currency(0.74, "USD")
    assert c.convert(Currency(1, "EUR"), "USD") != Currency(1000000, "USD")


test_different_currency_code_error()
test_are_ne()
test_are_eq_same_style()
test_are_eq_diff_style()
test_add_instances()
test_sub_instances()
test_mul_()
test_rmul_()
test_conversion()
