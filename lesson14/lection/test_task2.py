import unittest

from lesson14.lection import task
from task import is_prime
import doctest


class TestTask(unittest.TestCase):

    def test_is_prime(self):
        self.assertFalse(is_prime(42))
        self.assertTrue(is_prime(13))


def load_tests(tests):
    tests.addTests(doctest.DocTestSuite(task))
    tests.addTests(doctest.DocTestSuite('task.py'))
    return tests


if __name__ == '__main__':
    unittest.main()
