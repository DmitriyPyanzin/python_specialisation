# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь
import task3


class Employee(task3.Person):
    def __init__(self, name, patronymic, lastname, day_to_born, id_user):
        self.id_user = '0' * (6 - len(str(id_user))) + str(id_user)
        self.level = int(self.id_user) % 7
        super().__init__(name, patronymic, lastname, day_to_born)

    @property
    def get_id(self):
        return self.id_user

    @property
    def get_level(self):
        return self.level

if __name__ == '__main__':

    e = Employee('Дмитрий', 'Викторович', 'Пьянзин', '03.12.1987', 777)
    
    print(e.get_name())
    print(e.day_to_born)
    print(e.age)
    print(e.get_id)
    print(e.get_level)