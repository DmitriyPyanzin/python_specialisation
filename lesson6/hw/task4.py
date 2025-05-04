# Создайте модуль и напишите в нём функцию, которая получает на вход дату в
# формате DD.MM.YYYY Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна. Для простоты договоримся, что год
# может быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999
# года) действует Григорианский календарь. Проверку года на високосность
# вынести в отдельную защищённую функцию.

def check_date(date: str) -> bool:
    lst = [int(el) for el in date.split('.')]
    lst30_days = [4, 6, 9, 11]
    if 0 < lst[0] < 32 and 0 < lst[1] < 13 and 0 < lst[2] < 10000:
        if lst[1] == 2:
            def leap_year():
                return (lst[2] % 4 == 0 or lst[2] % 400 == 0) and lst[2] % 100 != 0
            if leap_year() and lst[0] > 29 or leap_year() == False and lst[0] > 28:
                return False
        elif lst[1] in lst30_days and lst[0] == 31:
            return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    print(check_date('09.04.2025'))
    