from ObjectOriented.Bank import BankAccount


class SavingsAccount(BankAccount):

    def __init__(self, balance):
        super().__init__(balance)
        self.balance = 500

    def withdraw(self, amount_to_withdraw):
        if self.balance <= 500:
            return "Cannot withdraw beyond the minimum account balance"
        return self.balance

    def deposit(self, amount):
        return self.balance
