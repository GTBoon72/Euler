import unittest
from SelfPowers import selfPowers, main as SP_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        SP_main()
        sys.stdout = sys.__stdout__
        self.assertIn("9110846700",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(selfPowers(10),10405071317)

    def test_value_errors(self):
        self.assertRaises(ValueError, selfPowers, -1)
        self.assertRaises(ValueError, selfPowers, 0)
        self.assertRaises(ValueError, selfPowers, 10**10)

    def test_type_errors(self):
        self.assertRaises(TypeError, selfPowers, "1")
        self.assertRaises(TypeError, selfPowers, 3+5j)
        self.assertRaises(TypeError, selfPowers, 1,0,1)

if __name__ == '__main__':
    unittest.main()