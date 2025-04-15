import unittest
import math
from calculator import add, sub, div, log

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

if __name__ == '__main__':
    unittest.main()