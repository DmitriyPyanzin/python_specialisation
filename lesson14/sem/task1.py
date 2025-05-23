# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

from string import ascii_lowercase


def only_english(word):
    """
    >>> only_english('EN32434GLISH LEываTTEвыаRS Aыва454ND SPA:%№:;:CES')
    'english letters and spaces'

    :param word: набор букв
    :return: Латиница в нижнем регистре и пробелы
    """
    return ''.join([el for el in word.lower() if el in ascii_lowercase or el == ' '])


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
