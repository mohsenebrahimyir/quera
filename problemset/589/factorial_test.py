#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/589/ ###

import unittest
from unittest.mock import patch

from factorial import factorial


class TestListMatchSearchs(unittest.TestCase):

    @patch('builtins.input', return_value=5)
    def test_factorial_5(self, mock_inputs):
        result = factorial()
        self.assertEqual(result, 120)


if __name__ == '__main__':
    unittest.main()

