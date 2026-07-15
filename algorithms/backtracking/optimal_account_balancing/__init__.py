from typing import List, DefaultDict
from collections import defaultdict


def min_transfers_dfs(transactions: List[List[int]]) -> int:
    if not transactions:
        return 0

    # Net balances where the key is the person and the value is their balance
    net_balances: DefaultDict[int, int] = defaultdict(int)

    # Populate net balances
    for transaction in transactions:
        sender, receiver, amount = transaction
        net_balances[sender] -= amount
        net_balances[receiver] += amount

    # Remove zero balances
    non_zero_balances = [amt for amt in net_balances.values() if amt != 0]
    number_of_non_zero_balances = len(non_zero_balances)

    if non_zero_balances == 0:
        return 0

    def dfs(current: int, balances: List[int]) -> int:
        # Skip settled accounts, move to the next person with non-zero balaance
        while current < number_of_non_zero_balances and balances[current] == 0:
            current += 1
        # All accounts settled
        if current >= number_of_non_zero_balances:
            return 0

        min_transactions = float("inf")
        # Try to settle non_zero_balances[start] by paring with another opposite sign balance
        for j in range(current + 1, number_of_non_zero_balances):
            # One owes, the other is owed
            if balances[current] * balances[j] < 0:
                balances[j] += balances[current]
                # recurse for remaining transactions after settling this one
                min_transactions = min(min_transactions, 1 + dfs(current + 1, balances))
                # backtrack, undo the settlement
                non_zero_balances[j] -= non_zero_balances[current]

        return min_transactions

    return dfs(0, non_zero_balances)


def min_transfers_backtrack(transactions: List[List[int]]) -> int:
    if not transactions:
        return 0

    # Net balances where the key is the person and the value is their balance
    net_balances: DefaultDict[int, int] = defaultdict(int)

    # Populate net balances
    for transaction in transactions:
        sender, receiver, amount = transaction
        net_balances[sender] -= amount
        net_balances[receiver] += amount

    # Remove zero balances
    non_zero_balances = [amt for amt in net_balances.values() if amt != 0]
    number_of_non_zero_balances = len(non_zero_balances)

    if non_zero_balances == 0:
        return 0

    def backtrack(start: int) -> int:
        # Skip settled accounts
        while start < number_of_non_zero_balances and non_zero_balances[start] == 0:
            start += 1
        # All accounts settled
        if start >= number_of_non_zero_balances:
            return 0

        min_transactions = float("inf")
        # Try to settle non_zero_balances[start] by paring with another opposite sign balance
        for j in range(start + 1, number_of_non_zero_balances):
            # One owes, the other is owed
            if non_zero_balances[start] * non_zero_balances[j] < 0:
                non_zero_balances[j] += non_zero_balances[start]
                # recurse for remaining transactions after settling this one
                min_transactions = min(min_transactions, 1 + backtrack(start + 1))
                # backtrack, undo the settlement
                non_zero_balances[j] -= non_zero_balances[start]
                if non_zero_balances[j] + non_zero_balances[start] == 0:
                    break
        return min_transactions

    return backtrack(0)
