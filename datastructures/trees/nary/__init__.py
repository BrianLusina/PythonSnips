from typing import List, Any
from .. import Tree, TreeNode


class NAryTree(Tree):
    def __init__(self, root: TreeNode):
        self.root = root

    def __len__(self) -> int:
        pass

    def next(self) -> int:
        pass

    def height(self) -> int:
        pass

    def lowest_common_ancestor(self, node_one: TreeNode, node_two: TreeNode) -> TreeNode:
        pass

    def has_next(self) -> bool:
        pass

    def increasing_order_traversal(self) -> TreeNode:
        pass

    def pre_order_traversal(self) -> List[Any]:
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

    def insert_node(self, value) -> TreeNode:
        pass

    def paths(self) -> list:
        pass
