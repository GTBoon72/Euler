import unittest
from PandigitalProducts import UniquePandigitalProducts as UPP, main as PP_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        PP_main()
        sys.stdout = sys.__stdout__
        self.assertIn("45228",capturedOutput.getvalue())

if __name__ == '__main__':
    unittest.main()