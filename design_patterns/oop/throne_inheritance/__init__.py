from collections import defaultdict
from typing import List


class ThroneInheritance:

    def __init__(self, king_name: str):
        self.king = king_name
        self.family_tree = defaultdict(list)
        self.inheritance_order = []
        self.dead = set()

    def _dfs(self, current) -> None:
        if current not in self.dead:
            self.inheritance_order.append(current)
        for child in self.family_tree[current]:
            self._dfs(child)

    def birth(self, parent_name: str, child_name: str) -> None:
        self.family_tree[parent_name].append(child_name)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def get_inheritance_order(self) -> List[str]:
        self.inheritance_order = []
        self._dfs(self.king)
        return self.inheritance_order
