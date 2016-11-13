from abc import ABCMeta, abstractmethod


class BankAccount(object):

    __metaclass__ = ABCMeta

    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount_to_withdraw):
        """
        Withdraw from the bank account
        :param amount_to_withdraw amount to withdraw from account
        :return:the new balance in account
        """
        if amount_to_withdraw > self.balance:
            return "Cannot withdraw beyond the current account balance"
        elif amount_to_withdraw < 0:
            return "Invalid withdraw amount"
        else:
            self.balance -= amount_to_withdraw

    @abstractmethod
    def deposit(self, amount):
        """
        Deposit into the bank account
        :param amount the amount to deposit in bank account
        :return:New balance in account
        """
        if amount < 0:
            return "Invalid deposit amount."
        else:
            self.balance += amount
