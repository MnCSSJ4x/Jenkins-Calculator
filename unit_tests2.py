#!/usr/bin/python3
import unittest
import math
from Calculator import advanced_calculator
from Calculator import cannot_be_computed


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = advanced_calculator()

    def test_case1(self):
        self.assertEqual(self.calculator.sqroot(-69), cannot_be_computed)

    def test_case2(self):
        self.assertEqual(self.calculator.factorial(-2), cannot_be_computed)


if __name__ == '__main__':
    unittest.main()
