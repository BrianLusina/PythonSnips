import json
from typing import Dict, List, Optional


def json_io(func):
    """
    Decorator to convert the return value of a function to JSON.
    @param func:
    @return:
    """

    def wrapper(self, url: str, payload: Optional[str] = None):
        if payload:
            payload = json.loads(payload)
        return json.dumps(func(self, url, payload), indent=2)

    return wrapper


class User:
    def __init__(
        self,
        name: str,
        owes: Optional[Dict[str, float]] = None,
        owed_by: Optional[Dict[str, float]] = None,
        **kwargs,
    ):
        if name != "":
            self.name = name
        else:
            raise ValueError("Name cannot be empty")
        self.records = {}
        for borrower, amount in (owed_by or {}).items():
            self.loan(borrower, amount)
        for lender, amount in (owes or {}).items():
            self.borrow(lender, amount)

    def borrow(self, borrower, amount):
        self.records[borrower] = self.records.get(borrower, 0) - amount

    def loan(self, lender, amount):
        self.records[lender] = self.records.get(lender, 0) + amount

    @property
    def owes(self):
        return {k: -v for k, v in self.records.items() if v < 0}

    @property
    def owed_by(self):
        return {k: v for k, v in self.records.items() if v > 0}

    @property
    def balance(self):
        return sum(self.records.values())

    def __str__(self):
        return f"{self.name} owes {self.owes} and is owed by {self.owed_by} with a balance of {self.balance}"

    def __repr__(self):
        return f"{self.name} owes {self.owes} and is owed by {self.owed_by} with a balance of {self.balance}"

    @property
    def __dict__(self):
        return {
            "name": self.name,
            "owes": self.owes,
            "owed_by": self.owed_by,
            "balance": self.balance,
        }


class RestAPI:
    def __init__(self, database: Optional[Dict[str, List[Dict]]] = None):
        self.database = {
            user["name"]: User(**user) for user in (database or {}).get("users", [])
        }

    @json_io
    def get(
        self, url: str, payload: Optional[Dict[str, List]] = None
    ) -> Optional[Dict]:
        if url == "/users":
            return {
                "users": [
                    user.__dict__
                    for name, user in sorted(self.database.items())
                    if payload is None or name in payload["users"]
                ]
            }

    @json_io
    def post(self, url: str, payload: Optional[Dict] = None) -> Optional[Dict]:
        if url == "/add":
            user = User(payload["user"])
            self.database[user.name] = user
            return user.__dict__

        if url == "/iou":
            lender = self.database[payload["lender"]]
            borrower = self.database[payload["borrower"]]
            amount = payload["amount"]
            lender.loan(borrower.name, amount)
            borrower.borrow(lender.name, amount)
            return {
                "users": sorted(
                    [lender.__dict__, borrower.__dict__], key=lambda x: x["name"]
                )
            }
