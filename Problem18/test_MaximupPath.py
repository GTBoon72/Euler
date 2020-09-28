import unittest
from MaximumPath import main as MP_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        MP_main()
        sys.stdout = sys.__stdout__
        self.assertIn("1074",capturedOutput.getvalue())

if __name__ == '__main__':
    unittest.main()
