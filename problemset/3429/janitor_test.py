#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/3429/ ###


import unittest
from unittest.mock import patch

from janitor import samovar_temperature


class TestListMatchSearchs(unittest.TestCase):
        
    @patch('builtins.input', return_value=110)
    def test_temperature_110(self, mock_inputs):
        result = samovar_temperature()
        self.assertEqual(result, "Steam")
        
    @patch('builtins.input', return_value=100)
    def test_temperature_100(self, mock_inputs):
        result = samovar_temperature()
        self.assertEqual(result, "Water")
        
    @patch('builtins.input', return_value=-200)
    def test_temperature_minus_200(self, mock_inputs):
        result = samovar_temperature()
        self.assertEqual(result, "Ice")


if __name__ == '__main__':
    unittest.main()