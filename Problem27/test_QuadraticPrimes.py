import unittest
from QuadraticPrimes import qprimes, main as QP_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        QP_main()
        sys.stdout = sys.__stdout__
        self.assertIn("-59231",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(qprimes(),(-61,971,71))

    def test_type_errors(self):
        self.assertRaises(TypeError, qprimes, "Test")
        self.assertRaises(TypeError, qprimes, 3+5j)
        self.assertRaises(TypeError, qprimes, 1,0,1)

if __name__ == '__main__':
    unittest.main()