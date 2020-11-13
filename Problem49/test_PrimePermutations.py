import unittest
from PrimePermutations import validPermutations, main as PP_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        PP_main()
        sys.stdout = sys.__stdout__
        self.assertIn("296962999629",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(validPermutations(4)[0],['1487', '4817', '8147'])

    def test_value_errors(self):
        self.assertRaises(ValueError, validPermutations, -1)
        self.assertRaises(ValueError, validPermutations, 0)
        self.assertRaises(ValueError, validPermutations, 10**10)

    def test_type_errors(self):
        self.assertRaises(TypeError, validPermutations, "1")
        self.assertRaises(TypeError, validPermutations, 3+5j)
        self.assertRaises(TypeError, validPermutations, 1,0,1)

if __name__ == '__main__':
    unittest.main()