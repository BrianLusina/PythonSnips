import json
from typing import Dict, Optional, List


class User:
    def __init__(self, name: str, owes: Optional[Dict[str, float]] = None, owed_by: Optional[Dict[str, float]] = None,
                 balance: Optional[float] = None):
        if name != "":
            self.name = name
        else:
            raise ValueError("Name cannot be empty")
        self.owes = owes or {}
        self.owed_by = owed_by or {}
        self.balance = balance or 0.0

    def __str__(self):
        return f"{self.name} owes {self.owes} and is owed by {self.owed_by} with a balance of {self.balance}"

    def __repr__(self):
        return f"{self.name} owes {self.owes} and is owed by {self.owed_by} with a balance of {self.balance}"

    def to_dict(self):
        return {
            "name": self.name,
            "owes": self.owes,
            "owed_by": self.owed_by,
            "balance": self.balance
        }


class RestAPI:
    def __init__(self, database: Optional[Dict[str, List[Dict]]] = None):
        self.database = self.initialize_database(database) if database else {"users": []}

    @staticmethod
    def initialize_database(database: Dict[str, List[Dict]]) -> Dict[str, List[User]]:
        db = {"users": []}
        for user in database["users"]:
            name, owes, owed_by, balance = user["name"], user["owes"], user["owed_by"], user["balance"]
            db["users"].append(User(name, owes, owed_by, balance))
        return db

    def __update(self):
        for user in self.database["users"]:
            owed_by = user.owed_by
            owes = user.owes
            for debtor in list(owed_by.keys()):
                if debtor in owes:
                    diff = 0
                    if debtor in owes:
                        diff = owes[debtor]
                        del owes[debtor]
                    if debtor in owed_by:
                        diff -= owed_by[debtor]
                        del owed_by[debtor]
                    if diff > 0:
                        owes[debtor] = diff
                    elif diff < 0:
                        owed_by[debtor] = -diff
            user.balance = sum(owed_by.values()) - sum(owes.values())

    def get(self, url: str, payload: Optional[str] = None) -> Optional[str]:
        if url == "/users":
            if not payload:
                return json.dumps(self.database)
            if payload is not None:
                payload = json.loads(payload)
                res = {"users": []}
                for user in self.database["users"]:
                    if user.name in payload["users"]:
                        res["users"].append(user.to_dict())
                return json.dumps(res)
        return None

    def post(self, url: str, payload: Optional[str] = None) -> Optional[str]:
        if url == "/add":
            if payload:
                data = json.loads(payload)
                name = data["user"]
                user = None
                users = self.database["users"]
                for u in users:
                    if u.name == name:
                        user = u
                        break
                if user is None:
                    new_user = User(name)
                    users.append(new_user)
                    self.__update()
                    return json.dumps(new_user.to_dict())
        if url == "/iou":
            if payload:
                data = json.loads(payload)
                lender_name, borrower_name, amount = data["lender"], data["borrower"], data["amount"]
                lender = borrower = None
                for user in self.database["users"]:
                    if user.name == lender_name:
                        lender = user
                    elif user.name == borrower_name:
                        borrower = user
                if lender and borrower:
                    lender.owed_by.setdefault(borrower_name, 0.0)
                    lender.owed_by[borrower_name] += amount
                    borrower.owes.setdefault(lender_name, 0.0)
                    borrower.owes[lender_name] += amount
                    self.__update()
                    return self.get('/users', json.dumps({'users': [lender_name, borrower_name]}))
        return None
