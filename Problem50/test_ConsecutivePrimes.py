import unittest
from ConsecutivePrimes import ConsecutivePrimes, main as CP_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        CP_main()
        sys.stdout = sys.__stdout__
        self.assertIn("997651",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(ConsecutivePrimes(100),[6, 41])
        self.assertEqual(ConsecutivePrimes(1000),[21, 953])

    def test_value_errors(self):
        self.assertRaises(ValueError, ConsecutivePrimes, -1)
        self.assertRaises(ValueError, ConsecutivePrimes, 0)
        self.assertRaises(ValueError, ConsecutivePrimes, 10**10)

    def test_type_errors(self):
        self.assertRaises(TypeError, ConsecutivePrimes, "1")
        self.assertRaises(TypeError, ConsecutivePrimes, 3+5j)
        self.assertRaises(TypeError, ConsecutivePrimes, 1,0,1)

if __name__ == '__main__':
    unittest.main()