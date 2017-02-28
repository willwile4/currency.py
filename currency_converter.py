from currency import Currency


# init with a currency dict
# work to convert two curr first
# must take a currency, and the requested currency
# and return a currency object equal to the current currency
#
# must take a currency, covert it to requested currency, and return
# the new currency object
# must be able to use a dictionary of three or more codes_dict
# must be able to convert curr to any other curr
# raises UnknownCurrencyCodeError if there is an unknown curr


class UnknownCurrencyCodeError(ValueError):
    pass


class CurrencyConverter:

    def __init__(self, rate_dict):
        self.rate_dict = rate_dict

    def __str__(self):
        return "We will convert any currency that we know"

    def __eq__(self, other):
        return self.rate_dict == self.rate_dict

    def convert(self, currency_obj, curr_code):
        if curr_code not in self.rate_dict.keys():
            raise UnknownCurrencyCodeError
        else:
            if currency_obj.code == curr_code:
                return currency_obj
            else:
                return Currency(str(currency_obj.val * self.rate_dict[curr_code]), curr_code)


c = Currency("500", "USD")
d = CurrencyConverter(sample_dict)
e = Currency("7", "GBP")
f = Currency("10", "KRW")
g = Currency("2100", "JPY")
print(c)
print(d.convert(c, "USD"))
print(d.convert(c, "EUR"))
print(d.convert(c, "GBP"))
print(d.convert(e, "JPY"))
print(d.convert(f, "USD")) # doesn't convert back to USD correctly.
print(d.convert(g, "KRW"))
print(d)
