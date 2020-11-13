import unittest
from DistinctPrimeFactors import consecutiveNumbers as cN, main as DPF_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        DPF_main()
        sys.stdout = sys.__stdout__
        self.assertIn("134043",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(cN(2),14)
        self.assertEqual(cN(3),644)

    def test_value_errors(self):
        self.assertRaises(ValueError, cN, -1)
        self.assertRaises(ValueError, cN, 0)
        self.assertRaises(ValueError, cN, 10**10)

    def test_type_errors(self):
        self.assertRaises(TypeError, cN, "1")
        self.assertRaises(TypeError, cN, 3+5j)
        self.assertRaises(TypeError, cN, 1,0,1)

if __name__ == '__main__':
    unittest.main()