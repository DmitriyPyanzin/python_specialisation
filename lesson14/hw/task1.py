class InsufficientFundsError(Exception):
    def __init__(self):
        super().__init__('Недостаточно средств')


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Сумма депозита должна быть положительной.')
        self.balance += amount

    def withdraw(self, amount):
        if amount > 0:
            raise InsufficientFundsError()
        self.balance -= amount

    @property
    def get_balance(self):
        return self.balance
