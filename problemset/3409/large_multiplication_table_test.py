#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/3409/ ###

import unittest
from unittest.mock import patch

from matplotlib.pyplot import table

from large_multiplication_table import multiple_table


class TestListMatchSearchs(unittest.TestCase):
        
    @patch('builtins.input', return_value=5)
    def test_multiple_table_5(self, mock_inputs):
        with open("5.txt") as f:
            table = f.read().strip()
        result = multiple_table()
        self.assertEqual(result, table)
        
    @patch('builtins.input', return_value=11)
    def test_multiple_table_11(self, mock_inputs):
        with open("11.txt") as f:
            table = f.read().strip()
        result = multiple_table()
        self.assertEqual(result, table)


if __name__ == '__main__':
    unittest.main()