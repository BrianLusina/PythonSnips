class BankAccount(object):
    def __init__(self):
        pass

    def withdraw(self, amount_to_withdraw):
        """
        Withdraw from the bank account
        :param amount_to_withdraw amount to withdraw from account
        :return:
        """
        pass

    def deposit(self, amount):
        """
        Deposit into the bank account
        :param amount the amount to deposit in bank account
        :return:New balance in account
        """
        pass


class SavingsAccount(BankAccount):

    def __init__(self):
        super(SavingsAccount, self).__init__()
        self.balance = 500

    def withdraw(self, amount_to_withdraw):
        try:
            if amount_to_withdraw > self.balance:
                return "Cannot withdraw beyond the current account balance"
            elif amount_to_withdraw < 0:
                return "Invalid withdraw amount"
            elif (self.balance - amount_to_withdraw) < 500:
                return "Cannot withdraw beyond the minimum account balance"
            else:
                self.balance -= amount_to_withdraw
            return self.balance
        except TypeError:
            return "Invalid withdraw amount"

    def deposit(self, amount):
        try:
            if amount > 0:
                self.balance += amount
                return self.balance
            else:
                return "Invalid deposit amount"
        except TypeError:
            return "Invalid deposit amount"


class CurrentAccount(BankAccount):

    def __init__(self):
        super(CurrentAccount, self).__init__()
        self.balance = 0

    def withdraw(self, amount_to_withdraw):
        try:
            if amount_to_withdraw < 0 or not isinstance(amount_to_withdraw, int):
                return "Invalid withdraw amount"
            elif amount_to_withdraw > self.balance:
                return "Cannot withdraw beyond the current account balance"
            elif (self.balance - amount_to_withdraw) < 500:
                return "Cannot withdraw beyond the minimum account balance"
            else:
                self.balance -= amount_to_withdraw
            return self.balance
        except TypeError:
            return "Invalid withdraw amount"

    def deposit(self, amount):
        try:
            if amount < 0:
                return "Invalid deposit amount."
            self.balance += amount
            return self.balance
        except TypeError:
            return "Invalid deposit amount"
