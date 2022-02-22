#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/9774/ ###
 
import unittest
from unittest.mock import patch

from print_number import print_num


class TestListMatchSearchs(unittest.TestCase):
        
    @patch('builtins.input', return_value=50943)
    def test_print_number_50943(self, mock_inputs):
        with open("50943.txt") as f:
            table = f.read().strip()
        result = print_num()
        self.assertEqual(result, table)

if __name__ == '__main__':
    unittest.main()