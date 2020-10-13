import unittest
from CircularPrimes import circularPrimes, main as CP_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        CP_main()
        sys.stdout = sys.__stdout__
        self.assertIn("55",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(len(circularPrimes(10**2)),13)
        self.assertEqual(circularPrimes(2),[2])

    def test_value_errors(self):
        self.assertRaises(ValueError, circularPrimes, -1)
        self.assertRaises(ValueError, circularPrimes, 0)
        self.assertRaises(ValueError, circularPrimes, 10**10)

    def test_type_errors(self):
        self.assertRaises(TypeError, circularPrimes, "Test")
        self.assertRaises(TypeError, circularPrimes, 3+5j)
        self.assertRaises(TypeError, circularPrimes, 1,0,1)

if __name__ == '__main__':
    unittest.main()