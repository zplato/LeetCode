# Abstract Class
from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    @abstractmethod
    def get_balance(self):
        pass

class CheckingAccount(BankAccount):
    def __init__(self, balance, overdraft_fee):
        super().__init__(balance)
        self._overdraft_fee = overdraft_fee

    def withdraw(self, amount):
        if amount > self._balance:
            self._balance -= (amount + self._overdraft_fee)
        else:
            self._balance -= amount

    def get_balance(self):
        print("Current Checking Account Balance: {0}".format(self._balance))

class SavingsAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)
        self._interest_rate = 0.01

    def apply_interest(self):
        self._balance += (self._balance * self._interest_rate)

    def get_balance(self):
        print("Current Savings Account Balance: {0}".format(self._balance))

class HighYieldSavingsAccount(SavingsAccount):
    def __init__(self, balance):
        super().__init__(balance)
        self._interest_rate = 0.1
        self._minimum_qualified_amount = 1000
        self._qualified = self._check_qualifications()

    def _check_qualifications(self):
        if self._balance > self._minimum_qualified_amount:
            print("Balance Qualified!")
            return True
        else:
            print(f"Balance doesn't qualify, need at least {self._minimum_qualified_amount}")
            return False



def main():
    my_savings = SavingsAccount(balance=100)
    my_checking = CheckingAccount(balance=500, overdraft_fee=25)

    my_savings.deposit(100)
    my_savings.apply_interest()
    my_savings.get_balance()

    my_checking.get_balance()
    my_checking.deposit(100)
    my_checking.get_balance()
    my_checking.withdraw(1100)
    my_checking.get_balance()

    # High Yield Savings
    my_hysa = HighYieldSavingsAccount(balance=999)
    my_hysa.apply_interest()
    my_hysa.deposit(1)
    my_hysa.apply_interest()


if __name__ == "__main__":
    main()


