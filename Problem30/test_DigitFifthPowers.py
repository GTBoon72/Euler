import unittest
from DigitFifthPowers import SumOfDigitPowers, main as DFP_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        DFP_main()
        sys.stdout = sys.__stdout__
        self.assertIn("443839",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(SumOfDigitPowers(4),'19316')
        self.assertEqual(SumOfDigitPowers(3),'1301')

    def test_value_errors(self):
        self.assertRaises(ValueError, SumOfDigitPowers, -1)
        self.assertRaises(ValueError, SumOfDigitPowers, 1)
        self.assertRaises(ValueError, SumOfDigitPowers, 7)

    def test_type_errors(self):
        self.assertRaises(TypeError, SumOfDigitPowers, "Test")
        self.assertRaises(TypeError, SumOfDigitPowers, 3+5j)
        self.assertRaises(TypeError, SumOfDigitPowers, 1,0,1)

if __name__ == '__main__':
    unittest.main()