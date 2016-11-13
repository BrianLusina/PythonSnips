from ObjectOriented.Bank import BankAccount


class SavingsAccount(BankAccount):

    def __init__(self):
        super().__init__()
        self.balance = 500

    def withdraw(self, amount_to_withdraw):
        if amount_to_withdraw > self.balance:
            return "Cannot withdraw beyond the current account balance"
        if self.balance <= 500:
            return "Cannot withdraw beyond the minimum account balance"
        if amount_to_withdraw < 0:
            return "Invalid withdraw amount"
        self.balance -= amount_to_withdraw
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        return "Invalid deposit amount"
