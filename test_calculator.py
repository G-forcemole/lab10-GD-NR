#https://github.com/G-forcemole/lab10-GD-NR/blob/main/test_calculator.py
# Partner 1: Gabriel Dos Santos
# Partner 2: Noah Robinson



import unittest
import math
from calculator import add, sub, div, log, multiply, log, hypotenuse, square_root


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-2, 5), 3)
        self.assertAlmostEqual(add(2.5, 3.5), 6.0)

    def test_subtract(self):
        # Test subtraction with various inputs.
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(5, 10), -5)
        self.assertAlmostEqual(sub(7.5, 2.5), 5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    def test_logarithm(self):
        result = log(10, 100)
        self.assertAlmostEqual(result, 2)
        result = log(math.e, math.e)
        self.assertAlmostEqual(result, 1)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 100)
        with self.assertRaises(ValueError):
            log(0, 100)
        with self.assertRaises(ValueError):
            log(-2, 10)

    def test_multiply(self):
       
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertAlmostEqual(multiply(2.5, 4), 10.0)

    def test_divide(self):
       a.
        self.assertEqual(div(2, 10), 5)   # 10 / 2 == 5
        self.assertEqual(div(4, 20), 5)   # 20 / 4 == 5

        self.assertEqual(div(2.5, 10.0), 4.0)

    def test_log_invalid_argument(self):

        with self.assertRaises(ValueError):
            log(1, 100)  # base 1 is invalid
        with self.assertRaises(ValueError):
            log(0, 100)  # base 0 is invalid
        with self.assertRaises(ValueError):
            log(-2, 10)  # negative base is invalid
        with self.assertRaises(ValueError):
            log(2, -10)  # negative argument is invalid
        with self.assertRaises(ValueError):
            log(2, 0)  # zero argument is invalid

    def test_hypotenuse(self):
        # Test that hypotenuse returns the correct Euclidean distance.
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(1.5, 2.5), math.hypot(1.5, 2.5))

    def test_sqrt(self):
        # Test that square_root returns the correct square root and handles negatives.
        self.assertAlmostEqual(square_root(16), 4.0)
        self.assertAlmostEqual(square_root(2.25), 1.5)
        with self.assertRaises(ValueError):
            square_root(-4)

if __name__ == '__main__':
        unittest.main()
