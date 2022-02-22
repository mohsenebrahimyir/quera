#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### Quera: https://quera.ir/problemset/2885/ ###


import unittest
from unittest.mock import patch

from a_simple_question import man_khoshghlab_hastam


class TestListMatchSearchs(unittest.TestCase):

    @patch('builtins.input', return_value=3)
    def test_factorial_5(self, mock_inputs):
        says = "man khoshghlab hastam\nman khoshghlab hastam\nman khoshghlab hastam"
        result = man_khoshghlab_hastam()
        self.assertEqual(result, says)


if __name__ == '__main__':
    unittest.main()
