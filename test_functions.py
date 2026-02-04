import unittest
import sys
from functions import *


class test_this(unittest.TestCase):

    def test_factorial(self):
        assert run_func(factorial) == None
    
    def test_iter(self):
        assert run_func(fact_iter) == None
    
    def test_fact_memo(self):
        assert run_func(fact_memo) == None


def run_func(f):
    for i in range(1000):
        f(i)
    return None

if __name__ == "__main__":
    sys.setrecursionlimit(1020)
    unittest.main()