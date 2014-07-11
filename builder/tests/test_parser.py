import unittest

from builder.fields import Field
from builder.parser import parse_field, parse_field_list

class TestParser(unittest.TestCase):
    def test_parse_field(self):
        def T(value, expected):
            actual = parse_field(value)
            self.assertEqual(actual, expected)
        T('TransactionVersion', Field.TransactionVersion)
        T('version', Field.TransactionVersion)
        T('transaction_version', Field.TransactionVersion)
        T('does_not_exist', None)
        T(None, None)

    def test_parse_field_list(self):
        def T(value, expected):
            actual = parse_field_list(value)
            self.assertEqual(actual, expected)
        a1 = ['TransactionVersion', 'TransactionType', 'CurrencyIdentifier',
              'NumberOfCoins']
        a2 = ['version', 'transaction_type', 'property_to_send',
              'amount_to_send']
        a3 = ['transaction_version', 'type', None, 'junk', 'currency_id',
              'amount']
        a4 = [None, 'junk']
        a5 = []
        expected = [Field.TransactionVersion,
                    Field.TransactionType,
                    Field.CurrencyIdentifier,
                    Field.NumberOfCoins]
        T(a1, expected)
        T(a2, expected)
        T(a3, expected)
        T(a4, [])
        T(a5, [])


if __name__ == '__main__':
    unittest.main()
