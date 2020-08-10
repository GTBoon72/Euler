import unittest
from NumberSpiralDiagonals import NumbersOnDiagonal, main as NSD_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        NSD_main()
        sys.stdout = sys.__stdout__
        self.assertIn("669171001",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(NumbersOnDiagonal(5),101)
        self.assertEqual(NumbersOnDiagonal(3),25)

    def test_value_errors(self):
        self.assertRaises(ValueError, NumbersOnDiagonal, -1)
        self.assertRaises(ValueError, NumbersOnDiagonal, 4)
        self.assertRaises(ValueError, NumbersOnDiagonal, 1)

    def test_type_errors(self):
        self.assertRaises(TypeError, NumbersOnDiagonal, "Test")
        self.assertRaises(TypeError, NumbersOnDiagonal, 3+5j)
        self.assertRaises(TypeError, NumbersOnDiagonal, 1,0,1)

if __name__ == '__main__':
    unittest.main()