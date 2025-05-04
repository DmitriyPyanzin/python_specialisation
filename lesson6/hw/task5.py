# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него
# напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно
# расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8
# ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 -
# координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют
# - ложь.

def exist_queen(place: tuple):
    return 0 < place[0] < 9 and 0 < place[1] < 9


def queens_movie(coord: tuple):
    lst_movie = []
    temp = [(col + 1, coord[1]) for col in range(8) if col + 1 != coord[0]]
    lst_movie += temp
    temp = [(coord[0], row + 1) for row in range(8) if row + 1 != coord[1]]
    lst_movie += temp
    temp = [(coord[0] + i, coord[1] + i) for i in range(1, 8) if coord[0] + i < 9 and coord[1] + i < 9]
    lst_movie += temp
    temp = [(coord[0] - i, coord[1] - i) for i in range(1, 8) if coord[0] - i > 0 and coord[1] - i > 0]
    lst_movie += temp
    temp = [(coord[0] - i, coord[1] + i) for i in range(1, 8) if coord[0] - i > 0 and coord[1] + i < 9]
    lst_movie += temp
    temp = [(coord[0] + i, coord[1] - i) for i in range(1, 8) if coord[0] + i < 9 and coord[1] - i > 0]
    lst_movie += temp
    return lst_movie


def pat(lst: list):
    lst_movies = []
    for i in range(8):
        if not exist_queen(lst[i]):
            return False
        lst_movies += [queens_movie(lst[i])]
    for j in range(8):
        for k in range(8):
            if lst[j] in lst_movies[k]:
                return False
    return True


print(pat([(1, 3), (2, 6), (3, 8), (4, 1), (5, 5), (6, 7), (7, 2), (8, 4)]))
