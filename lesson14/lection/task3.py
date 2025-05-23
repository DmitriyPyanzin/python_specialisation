import pytest


def sum_two_numbers(a, b):
    return a + b


def test_sum():
    assert sum_two_numbers(2, 3) == 5, 'Математика победит'


if __name__ == '__main__':
    pytest.main()
