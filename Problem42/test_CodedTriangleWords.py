import unittest
from CodedTriangleWords import wordValue as wV, main as CTW_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        CTW_main()
        sys.stdout = sys.__stdout__
        self.assertIn("162",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(wV('abc'),6)
        self.assertEqual(wV('ABC'),6)

#    def test_value_errors(self):
#        self.assertRaises(ValueError, wV, -1)
#        self.assertRaises(ValueError, wV, 0)
#        self.assertRaises(ValueError, wV, 10**10)

    def test_type_errors(self):
        self.assertRaises(TypeError, wV, "1")
        self.assertRaises(TypeError, wV, 3+5j)
        self.assertRaises(TypeError, wV, 1,0,1)

if __name__ == '__main__':
    unittest.main()