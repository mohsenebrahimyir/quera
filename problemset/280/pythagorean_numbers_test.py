#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/280/ ###

import unittest
from unittest.mock import patch

from pythagorean_numbers import pythagorean


class TestListTriangles(unittest.TestCase):

    searchs = [[8, 7, 10], [5, 4, 3]]

    @patch('builtins.input', side_effect=searchs[0])
    def test_is_a_right_triangle_no(self, mock_inputs):
        result = pythagorean()
        self.assertEqual(result, "NO")
        
    @patch('builtins.input', side_effect=searchs[1])
    def test_is_a_right_triangle_yes(self, mock_inputs):
        result = pythagorean()
        self.assertEqual(result, "YES")


if __name__ == '__main__':
    unittest.main()
