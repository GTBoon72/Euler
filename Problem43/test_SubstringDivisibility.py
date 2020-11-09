import unittest
from SubstringDivisibility import getPandigitals as gP, main as SD_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        SD_main()
        sys.stdout = sys.__stdout__
        self.assertIn("16695334890",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(len(gP()),6)
        self.assertIn(gP(),1406357289)

#    def test_value_errors(self):
#        self.assertRaises(ValueError, wV, -1)
#        self.assertRaises(ValueError, wV, 0)
#        self.assertRaises(ValueError, wV, 10**10)

    def test_type_errors(self):
        self.assertRaises(TypeError, gP, "1")
        self.assertRaises(TypeError, gP, 3+5j)
        self.assertRaises(TypeError, gP, 1,0,1)

if __name__ == '__main__':
    unittest.main()