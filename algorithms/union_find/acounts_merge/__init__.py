from typing import List, Dict

from collections import defaultdict

from datastructures import UnionFind


def accounts_merge(accounts: List[List[str]]) -> List[List[str]]:
    uf = UnionFind(len(accounts))
    # Map that stores emails to their parent IDs
    email_to_account_map: Dict[str, int] = dict()

    # iterate through the accounts
    for account_id, account in enumerate(accounts):
        # We iterate from the second position onwards for each account as those are the emails
        for email in account[1:]:
            # For this email check if the email is present in the mapping
            if email in email_to_account_map:
                uf.union(account_id, email_to_account_map[email])
            else:
                email_to_account_map[email] = account_id

    # create a map to store the merged accounts
    merged_accounts = defaultdict(list)
    for email, acc_id in email_to_account_map.items():
        root = uf.find(acc_id)
        merged_accounts[root].append(email)

    # sort the merged accounts
    result = []
    for i, emails in merged_accounts.items():
        name = accounts[i][0]
        result.append([name] + sorted(merged_accounts[i]))

    return result
