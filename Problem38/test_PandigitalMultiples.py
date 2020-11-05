import unittest
from PandigitalMultiples import main as PM_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        PM_main()
        sys.stdout = sys.__stdout__
        self.assertIn("932718654",capturedOutput.getvalue())

if __name__ == '__main__':
    unittest.main()