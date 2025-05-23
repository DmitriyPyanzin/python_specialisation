import pytest
from task1 import only_english


def test_only_english():
    assert only_english('Hello, world!') == 'hello world'


def test_not_only_english2():
    assert only_english('Hello, world!') != 'hello, world'


if __name__ == '__main__':
    pytest.main(['-v'])
