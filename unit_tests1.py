#!/usr/bin/python3
import unittest
import math
from Calculator import advanced_calculator


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = advanced_calculator()

    def test_case1(self):
        self.assertEqual(self.calculator.sqroot(49), 7)

    def test_case2(self):
        self.assertEqual(self.calculator.factorial(5), 120)

    def test_case3(self):
        self.assertEqual(self.calculator.natural_log(7), math.log(7))


if __name__ == '__main__':
    unittest.main()
