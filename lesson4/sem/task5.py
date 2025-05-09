# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

names = ["Коля", "Боря", "Анатолий"]
salaries = [10000, 20000, 30000]
prizes = ["10.25%", "11.40%", "12.50%"]

print({name: round(salary * float(prize.rstrip('%')) / 100, 2) for name, salary, prize in zip(names, salaries, prizes)})
