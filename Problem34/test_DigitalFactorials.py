import unittest
from DigitFactorials import sumDigitFactorial as sDF, main as DF_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        DF_main()
        sys.stdout = sys.__stdout__
        self.assertIn("40730",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(sDF(145),145)
        self.assertEqual(sDF(40585),40585)

    def test_value_errors(self):
        self.assertRaises(ValueError, sDF, -1)
        self.assertRaises(ValueError, sDF, 0)

    def test_type_errors(self):
        self.assertRaises(TypeError, sDF, "Test")
        self.assertRaises(TypeError, sDF, 1, 1)
        self.assertRaises(TypeError, sDF, 3+5j)

if __name__ == '__main__':
    unittest.main()