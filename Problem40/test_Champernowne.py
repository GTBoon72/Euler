import unittest
from Champernowne import calcChampernowne as cC, main as C_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        C_main()
        sys.stdout = sys.__stdout__
        self.assertIn("210",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(cC(1),'12345678910')

    def test_value_errors(self):
        self.assertRaises(ValueError, cC, -1)
        self.assertRaises(ValueError, cC, 0)
        self.assertRaises(ValueError, cC, 10**10)

    def test_type_errors(self):
        self.assertRaises(TypeError, cC, "Test")
        self.assertRaises(TypeError, cC, 3+5j)
        self.assertRaises(TypeError, cC, 1,0,1)

if __name__ == '__main__':
    unittest.main()