#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/10230/ ###


import unittest
from unittest.mock import patch

from homework_baqer import can_make_triangle_with_angles


class TestListMatchSearchs(unittest.TestCase):

    @patch('builtins.input', return_value="70 60 50 ")
    def test_homework_1(self, mock_inputs):
        result = can_make_triangle_with_angles()
        self.assertEqual(result, "Yes")

    @patch('builtins.input', return_value="180 0 0 ")
    def test_homework_2(self, mock_inputs):
        result = can_make_triangle_with_angles()
        self.assertEqual(result, "No")

    @patch('builtins.input', return_value="150 40 10 ")
    def test_homework_3(self, mock_inputs):
        result = can_make_triangle_with_angles()
        self.assertEqual(result, "No")

    @patch('builtins.input', return_value="78 102 0 ")
    def test_homework_4(self, mock_inputs):
        result = can_make_triangle_with_angles()
        self.assertEqual(result, "No")

    @patch('builtins.input', return_value="87 65 27 ")
    def test_homework_5(self, mock_inputs):
        result = can_make_triangle_with_angles()
        self.assertEqual(result, "No")


if __name__ == '__main__':
    unittest.main()