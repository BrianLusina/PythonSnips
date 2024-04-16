from typing import List, Any
from collections import deque
from .. import Tree, T
from .node import NAryNode


class NAryTree(Tree):
    def __init__(self, root: NAryNode):
        self.root = root

    def __len__(self) -> int:
        pass

    def is_balanced(self) -> bool:
        pass

    def leaf_similar(self, other: "Tree") -> bool:
        pass

    def number_of_good_nodes(self) -> int:
        pass

    def path_sum(self, target: T) -> int:
        pass

    def next(self) -> int:
        pass

    def height(self) -> int:
        pass

    def lowest_common_ancestor(
        self, node_one: NAryNode, node_two: NAryNode
    ) -> NAryNode:
        pass

    def has_next(self) -> bool:
        pass

    def increasing_order_traversal(self) -> NAryNode:
        pass

    def pre_order_traversal(self) -> List[T]:
        stack, visited = deque([]), []
        if not self.root:
            return visited

        stack.append(self.root)

        while stack:
            node = stack.pop()
            visited.append(node.data)
            stack.extend(node.children[::-1])

        return visited

    def level_order_traversal(self) -> List[Any]:
        values, queue = [], []
        if not self.root:
            return values

        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            values.append(node.data)

            for child in node.children:
                queue.append(child)

        return values

    def get_depth(self) -> int:
        pass

    def insert_node(self, value) -> NAryNode:
        pass

    def paths(self) -> list:
        pass
