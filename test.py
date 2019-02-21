import unittest
import subprocess
from sympy import *
class TestingOnlineCalculator(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(str(subprocess.check_output(['curl','http://localhost:5000/']).decode('ascii')),"Usage:curl -d 'A=val1&B=val2' -X POST http://localhost:5000/<oper>")
if __name__=='__main__':
    unittest.main()