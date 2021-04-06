from abc import ABCMeta, abstractmethod


class BankAccount(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def withdraw(self, amount_to_withdraw):
        """
        Withdraw from the bank account
        :param amount_to_withdraw amount to withdraw from account
        :return:
        """
        pass

    @abstractmethod
    def deposit(self, amount):
        """
        Deposit into the bank account
        :param amount the amount to deposit in bank account
        :return:New balance in account
        """
        pass
