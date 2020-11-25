import unittest
from PermutedMultiples import permutedMultiples as pM, main as PM_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        PM_main()
        sys.stdout = sys.__stdout__
        self.assertIn("142857",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(pM(2),125874)
        self.assertEqual(pM(6),142857)

    def test_value_errors(self):
        self.assertRaises(ValueError, pM, -1)
        self.assertRaises(ValueError, pM, 0)
        self.assertRaises(ValueError, pM, 11)

    def test_type_errors(self):
        self.assertRaises(TypeError, pM, "1")
        self.assertRaises(TypeError, pM, 3+5j)
        self.assertRaises(TypeError, pM, 1,0,1)

if __name__ == '__main__':
    unittest.main()