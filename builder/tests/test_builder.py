import unittest

from builder.fields import Field
from builder import create_transaction, decode_transaction

class TestBuilder(unittest.TestCase):
    def test_create(self):
        data = [(Field.TransactionVersion, 0),
                (Field.TransactionType, 0),
                (Field.CurrencyIdentifier, 3),
                (Field.NumberOfCoins, 12000)]
        expected = '00000000000000030000000000002ee0'
        actual = create_transaction(data)
        self.assertEqual(actual, expected)

    def test_decode(self):
        hex = '0000000000000001000000012a05f200'
        fields = [Field.TransactionVersion,
                  Field.TransactionType,
                  Field.CurrencyIdentifier,
                  Field.NumberOfCoins]
        expected = [(Field.TransactionVersion, 0),
                    (Field.TransactionType, 0),
                    (Field.CurrencyIdentifier, 1),
                    (Field.NumberOfCoins, 5000000000)]
        actual = decode_transaction(hex, fields)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
