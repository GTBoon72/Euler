import unittest
from PrimeDigitReplacements import firstPrimeInFamilyOfSize as PDR, main as PDR_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        PDR_main()
        sys.stdout = sys.__stdout__
        self.assertIn("121313",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(PDR(6),[13, [13, 23, 43, 53, 73, 83]])
        self.assertEqual(PDR(7),[56003, [56003, 56113, 56333, 56443, 56663, 56773, 56993]])

    def test_value_errors(self):
        self.assertRaises(ValueError, PDR, -1)
        self.assertRaises(ValueError, PDR, 0)
        self.assertRaises(ValueError, PDR, 11)

    def test_type_errors(self):
        self.assertRaises(TypeError, PDR, "1")
        self.assertRaises(TypeError, PDR, 3+5j)
        self.assertRaises(TypeError, PDR, 1,0,1)

if __name__ == '__main__':
    unittest.main()