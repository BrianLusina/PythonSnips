from ObjectOriented.Bank import BankAccount


class CurrentAccount(BankAccount):

    def __init__(self, balance):
        super().__init__(balance)
        self.balance = 0

    def withdraw(self, amount_to_withdraw):
        return self.balance

    def deposit(self, amount):
        return self.balance
