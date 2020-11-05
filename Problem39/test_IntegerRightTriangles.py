import unittest
from IntegerRightTriangles import IntegerRightTriangles as IRT, main as IRT_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        IRT_main()
        sys.stdout = sys.__stdout__
        self.assertIn("840",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(IRT(750),720)
        self.assertEqual(IRT(1000),840)

    def test_value_errors(self):
        self.assertRaises(ValueError, IRT, -1)
        self.assertRaises(ValueError, IRT, 0)
        self.assertRaises(ValueError, IRT, 10**10)

    def test_type_errors(self):
        self.assertRaises(TypeError, IRT, "Test")
        self.assertRaises(TypeError, IRT, 3+5j)
        self.assertRaises(TypeError, IRT, 1,0,1)

if __name__ == '__main__':
    unittest.main()