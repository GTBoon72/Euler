import unittest
from TriPentHexNumbers import TPH, main as TPH_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        TPH_main()
        sys.stdout = sys.__stdout__
        self.assertIn("1533776805",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(TPH(1),40755)

    def test_value_errors(self):
        self.assertRaises(ValueError, TPH, -1)
        self.assertRaises(ValueError, TPH, 0)
        self.assertRaises(ValueError, TPH, 10**10)

    def test_type_errors(self):
        self.assertRaises(TypeError, TPH, "1")
        self.assertRaises(TypeError, TPH, 3+5j)
        self.assertRaises(TypeError, TPH, 1,0,1)

if __name__ == '__main__':
    unittest.main()