def is_prime(num: int) -> bool:
    """
    Проверка числа на простоту.
    :param num: Передаваемое число
    :return: Истина или ложь
    >>> is_prime(42)
    False
    >>> is_prime(13)
    True
    """
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)
