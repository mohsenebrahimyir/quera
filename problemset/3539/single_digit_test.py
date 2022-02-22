#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/3539/ ##

import unittest
from unittest.mock import patch

from single_digit import single_digit


class TestListMatchSearchs(unittest.TestCase):

    @patch('builtins.input', return_value=14)
    def test_single_digit_14(self, mock_inputs):
        result = single_digit()
        self.assertEqual(result, 5)

    @patch('builtins.input', return_value=123456)
    def test_single_digit_123456(self, mock_inputs):
        result = single_digit()
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
