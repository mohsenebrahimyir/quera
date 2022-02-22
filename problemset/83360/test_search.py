import unittest
from unittest.mock import patch

from search import match_search


class TestListMatchSearchs(unittest.TestCase):

    searchs = [
        ["framework", "In cs, a string is traditionally a sequence of characters"],
        ["string", "string theory is a theoretical framework in particle physics"]
    ]

    @patch('builtins.input', side_effect=searchs[0])
    def test_search_0(self, mock_inputs):
        result = match_search()
        self.assertEqual(result, 0)
        
    @patch('builtins.input', side_effect=searchs[1])
    def test_search_1(self, mock_inputs):
        result = match_search()
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
