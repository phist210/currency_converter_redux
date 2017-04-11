#!/usr/bin/env python3
from currency import Currency


class DifferentCurrencyCodeError(Exception):
    pass


class UnknownCurrencyCodeError(Exception):
    pass


class CurrencyConverter:

    rates = {'USD': 1.0, 'EUR': 0.74, 'JPY': 120.0}

    def __init__(self):
        self.rates = CurrencyConverter.rates

    def convert(self, other, conversion_unit):

        if other.code in self.rates and conversion_unit in self.rates:
            new_amount = (other.amount * self.rates[conversion_unit]) / self.rates[other.code]
            return Currency(round(new_amount, 2), conversion_unit)
        else:
            raise UnknownCurrencyCodeError
