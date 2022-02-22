#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/616/ ###


import unittest
from unittest.mock import patch

from power_two import power_2


class TestListMatchSearchs(unittest.TestCase):
        
    @patch('builtins.input', return_value=95)
    def test_power_two_95(self, mock_inputs):
        result = power_2()
        self.assertEqual(result, 128)
        
    @patch('builtins.input', return_value=1010)
    def test_power_two_1010(self, mock_inputs):
        result = power_2()
        self.assertEqual(result, 1024)


if __name__ == '__main__':
    unittest.main()
