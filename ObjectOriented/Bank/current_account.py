from ObjectOriented.Bank import BankAccount


class CurrentAccount(BankAccount):

    def __init__(self):
        super().__init__()
        self.balance = 0

    def withdraw(self, amount_to_withdraw):
        if amount_to_withdraw < 0:
            return "Invalid withdraw amount"
        if amount_to_withdraw > self.balance:
            return "Cannot withdraw beyond the current account balance"
        self.balance -= amount_to_withdraw
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            return "Invalid deposit amount."
        self.balance += amount
        return self.balance
