import unittest
from DoubleBasePalindromes import isPalindromeInBothBases as iPIBB, PalindromesInBothBases as PIBB, main as DBP_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        DBP_main()
        sys.stdout = sys.__stdout__
        self.assertIn("872187",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(iPIBB(585),True)
        self.assertEqual(PIBB(2),[1])

    def test_value_errors(self):
        self.assertRaises(ValueError, PIBB, -1)
        self.assertRaises(ValueError, PIBB, 0)
        self.assertRaises(ValueError, PIBB, 10**10)

    def test_type_errors(self):
        self.assertRaises(TypeError, PIBB, "Test")
        self.assertRaises(TypeError, PIBB, 3+5j)
        self.assertRaises(TypeError, PIBB, 1,0,1)

if __name__ == '__main__':
    unittest.main()