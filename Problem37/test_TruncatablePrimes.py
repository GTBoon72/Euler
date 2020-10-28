import unittest
from TruncatablePrimes import truncatablePrimes as tP, main as TP_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        TP_main()
        sys.stdout = sys.__stdout__
        self.assertIn("748317",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(len(tP(5)),5)
        self.assertEqual(tP(1),[23])

    def test_value_errors(self):
        self.assertRaises(ValueError, tP, -1)
        self.assertRaises(ValueError, tP, 0)
        self.assertRaises(ValueError, tP, 10**10)

    def test_type_errors(self):
        self.assertRaises(TypeError, tP, "Test")
        self.assertRaises(TypeError, tP, 3+5j)
        self.assertRaises(TypeError, tP, 1,0,1)

if __name__ == '__main__':
    unittest.main()