#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/3537/ ###


import unittest
from unittest.mock import patch

from yellow_question import says_wow


class TestListMatchSearchs(unittest.TestCase):
        
    @patch('builtins.input', return_value=1)
    def test_says_wow_1(self, mock_inputs):
        result = says_wow()
        self.assertEqual(result, "Wow!")
        
    @patch('builtins.input', return_value=2)
    def test_says_wow_2(self, mock_inputs):
        result = says_wow()
        self.assertEqual(result, "Woow!")


if __name__ == '__main__':
    unittest.main()