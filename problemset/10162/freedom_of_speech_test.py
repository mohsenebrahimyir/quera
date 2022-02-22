#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/10162/ ###

import unittest
from unittest.mock import patch

from freedom_of_speech import bala_or_payin_barare


class TestListMatchSearchs(unittest.TestCase):

    @patch('builtins.input', return_value=1)
    def test_barare_1(self, mock_inputs):
        result = bala_or_payin_barare()
        self.assertEqual(result, "Payin Barare")

    @patch('builtins.input', return_value=74)
    def test_barare_74(self, mock_inputs):
        result = bala_or_payin_barare()
        self.assertEqual(result, "Bala Barare")


if __name__ == '__main__':
    unittest.main()
