import pytest
import task1


@pytest.fixture
def bank_account():
    return task1.BankAccount(100)


def test_balance(bank_account):
    assert bank_account.get_balance == 100


def test_deposit(bank_account):
    bank_account.deposit(50)
    assert bank_account.get_balance == 150


def test_withdraw(bank_account):
    bank_account.withdraw(30)
    assert bank_account.get_balance == 70


def test_withdraw_funds(bank_account):
    with pytest.raises(task1.InsufficientFundsError):
        bank_account.withdraw(200)


def test_deposit_negative(bank_account):
    with pytest.raises(ValueError):
        bank_account.deposit(-10)


if __name__ == '__main__':
    pytest.main(['-v'])
