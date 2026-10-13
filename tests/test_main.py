"""Модульные тесты функции factorial."""

import unittest

from main import factorial


class TestFactorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_five(self):
        self.assertEqual(factorial(5), 120)

    def test_ten(self):
        self.assertEqual(factorial(10), 3628800)

    def test_negative(self):
        with self.assertRaises(ValueError):
            factorial(-3)

    def test_float(self):
        with self.assertRaises(TypeError):
            factorial(2.5)

    def test_boolean(self):
        with self.assertRaises(TypeError):
            factorial(True)


if __name__ == "__main__":
    unittest.main()
