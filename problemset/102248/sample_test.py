#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/102248/ ###

import unittest
from moghayeseGar import compare


class Test(unittest.TestCase):
    
    def test_sample_1(self):
        self.assertEqual(compare('ali', 'salib'), 'las')
    
    def test_sample_2(self):
        self.assertEqual(compare('nima', 'amin'), 'Both strings are empty!')


if __name__ == '__main__':
    unittest.main()