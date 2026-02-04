import unittest
from functions import *


class test_this(unittest.TestCase):

    def test_factorial(self):
        self.assertIsNone(run_func(factorial))

    def test_iter(self):
        self.assertIsNone(run_func(fact_iter))

    def test_fact_memo(self):
        self.assertIsNone(run_func(fact_memo))


def run_func(f):
    for i in range(1000):
        f(i)
    return None


if __name__ == "__main__":
    unittest.main()
