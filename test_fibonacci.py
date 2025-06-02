import unittest
from fibonacci import calculate_fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_zero(self):
        self.assertEqual(calculate_fibonacci(0), 0)

    def test_fibonacci_one(self):
        self.assertEqual(calculate_fibonacci(1), 1)

    def test_fibonacci_small_positive(self):
        self.assertEqual(calculate_fibonacci(5), 5)

    def test_fibonacci_large_positive(self):
        self.assertEqual(calculate_fibonacci(13), 233)

    def test_fibonacci_negative_input(self):
        with self.assertRaises(ValueError):
            calculate_fibonacci(-1)

if __name__ == '__main__':
    unittest.main()
