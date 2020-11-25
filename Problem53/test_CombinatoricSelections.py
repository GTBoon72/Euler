import unittest
from CombinatoricSelections import validCombinations as vC, main as CS_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        CS_main()
        sys.stdout = sys.__stdout__
        self.assertIn("4075",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(vC(23,10**6),4)
        self.assertEqual(vC(100,10**6),4075)

    def test_value_errors(self):
        self.assertRaises(ValueError, vC, -1,10)
        self.assertRaises(ValueError, vC, 0,10)
        self.assertRaises(ValueError, vC, 1001,10)

    def test_type_errors(self):
        self.assertRaises(TypeError, vC, "1")
        self.assertRaises(TypeError, vC, 3+5j)
        self.assertRaises(TypeError, vC, 1,0,1)

if __name__ == '__main__':
    unittest.main()