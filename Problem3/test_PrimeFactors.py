import unittest
from PrimeFactors import get_prime_factors

class TestFunction(unittest.TestCase):
    def test_function(self):
        self.assertEqual(get_prime_factors(16), [2, 2, 2, 2])
        self.assertEqual(get_prime_factors(51), [3, 17])

    def test_value_errors(self):
        self.assertRaises(ValueError, get_prime_factors, 0)

    def test_type_errors(self):
        self.assertRaises(TypeError, get_prime_factors, "Test")
        self.assertRaises(TypeError, get_prime_factors, 3+5j)

if __name__ == '__main__':
    unittest.main()