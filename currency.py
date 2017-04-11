#!/usr/bin/env python3


class DifferentCurrencyCodeError(Exception):
        pass


class Currency:
    CURRENCY_CODE = {'USD': '$', 'EUR': '€', 'JPY': '¥', 'GBP': '£'}

    def __init__(self, amount, code=''):

        if code:
            self.code = code
            self.amount = amount
        else:
            for currency, symbol in self.CURRENCY_CODE.items():
                if amount[0] == symbol:
                    self.code = currency
                    self.amount = amount[1:]
        try:
            self.amount = float(self.amount)
        except ValueError:
            print("Can not convert str to float")

    def __add__(self, other):
        if self.code == other.code:
            new_amount = self.amount + other.amount
            return Currency(new_amount, self.code)
        else:
            raise DifferentCurrencyCodeError("Currency codes do not match")

    def __sub__(self, other):
        if self.code == other.code:
            new_amount = self.amount - other.amount
            return Currency(new_amount, self.code)
        else:
            raise DifferentCurrencyCodeError("Currency codes do not match")

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Currency(self.amount * other, self.code)
        else:
            raise DifferentCurrencyCodeError("Currency codes do not match")

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Currency(self.amount * other, self.code)
        else:
            raise DifferentCurrencyCodeError("Currency codes do not match")

    def __eq__(self, other):
        if not isinstance(other, Currency):
            return False
        return self.code == other.code and self.amount == other.amount

    def __ne__(self, other):
        if not isinstance(other, Currency):
            return False
        return self.code != other.code or self.amount != other.amount

    def __str__(self):
        return "{0}{1:0.2f}".format(self.CURRENCY_CODE[self.code], self.amount)
