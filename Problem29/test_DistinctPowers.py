import unittest
from DistinctPowers import Powers, main as DP_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        DP_main()
        sys.stdout = sys.__stdout__
        self.assertIn("9183",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(Powers(5,5),15)
        self.assertEqual(Powers(2,4),3)

    def test_value_errors(self):
        self.assertRaises(ValueError, Powers, -1,2)
        self.assertRaises(ValueError, Powers, 4,1)
        self.assertRaises(ValueError, Powers, 0,0)

    def test_type_errors(self):
        self.assertRaises(TypeError, Powers, "Test")
        self.assertRaises(TypeError, Powers, 3+5j)
        self.assertRaises(TypeError, Powers, 1,0,1)

if __name__ == '__main__':
    unittest.main()