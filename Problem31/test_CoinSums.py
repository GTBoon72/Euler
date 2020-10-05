import unittest
from CoinSums import numberOfCoinCombinations as nOCC, main as CS_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        CS_main()
        sys.stdout = sys.__stdout__
        self.assertIn("73682",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(nOCC(5,[1,2,5]),4)
        self.assertEqual(nOCC(11,[1,2,5,10]),12)

    def test_value_errors(self):
        self.assertRaises(ValueError, nOCC, -1,[1,2,5])
        self.assertRaises(ValueError, nOCC, 1,[0])
        self.assertRaises(ValueError, nOCC, 1,[2,1,1])

    def test_type_errors(self):
        self.assertRaises(TypeError, nOCC, 4,["a",1,2])
        self.assertRaises(TypeError, nOCC, "Test",[1,2,5])
        self.assertRaises(TypeError, nOCC, 3+5j,[1,2,5])

if __name__ == '__main__':
    unittest.main()