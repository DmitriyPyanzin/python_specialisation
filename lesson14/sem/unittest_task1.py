import unittest
from task1 import only_english


class TestCase(unittest.TestCase):
    def test_only_english(self):
        self.assertEqual(only_english('Hello, world!'), 'hello world')

    def test_not_only_english(self):
        self.assertNotEquals(only_english('Hello, world!'), 'hello, world')


if __name__ == '__main__':
    unittest.main(verbosity=2)
