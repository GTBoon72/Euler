import unittest
from DigitCancellingFractions import main as DCF_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        DCF_main()
        sys.stdout = sys.__stdout__
        self.assertIn("100",capturedOutput.getvalue())

if __name__ == '__main__':
    unittest.main()