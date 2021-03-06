# test file for currency.py
import unittest
from currency import Currency
from currency import DifferentCurrencyCodeError
from currency import InvalidInputError


class TestCurrencyCode(unittest.TestCase):
    # test __init__
    def setUp(self):
        self.test_a = Currency(4.50, "USD")
        self.test_1a = Currency("$4.50")
        self.test_b = Currency("$0.75")
        self.test_c = Currency("€5,00")
        self.test_d = Currency("¥2500")

    def test_currency_str_method(self):
        self.assertEqual(str(self.test_a), "4.50, USD")

    def test_currency_eq(self):
        self.assertTrue(self.test_a.__eq__(self.test_1a))

    def test_currency_not_eq(self):
        self.assertFalse(self.test_a == self.test_c)

    def test_valid_input_add(self):
        self.assertEqual(self.test_a.__add__(self.test_b), "$5.25")

    def test_invalid_input_add(self):
        with self.assertRaises(DifferentCurrencyCodeError):
            self.test_a.__add__(self.test_c)

    def test_valid_input_subtract(self):
        self.assertEqual(self.test_a - self.test_b, "$3.75")

    def test_invalid_input_sub(self):
        with self.assertRaises(DifferentCurrencyCodeError):
            self.test_a.__sub__(self.test_d)

    def test_valid_input_mul(self):
        self.assertEqual(self.test_a.__mul__(5), "$22.50")

    def test_invalid_input_mul(self):
        with self.assertRaises(TypeError):
            self.test_a.__mul__.self.test_d)


if __name__ == '__main__':
    unittest.main()
