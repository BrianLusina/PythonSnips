from typing import Optional, List
from datastructures.trees import Tree, TreeNode, T
from datastructures.trees.ternary.node import TernaryTreeNode


class TernaryTree(Tree):

    def __init__(self, root: Optional[TernaryTreeNode] = None):
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

    def get_depth(self) -> int:
        pass

    def insert_node(self, value) -> TreeNode:
        pass

    def paths(self) -> List[str]:

        def dfs(root: TernaryTreeNode, path: List, result: List):
            if all(c is None for c in root.children):
                result.append("->".join(path) + "->" + str(root.data))
                return
            for child in root.children:
                if child is not None:
                    path.append(str(root.data))
                    dfs(child, path, result)
                    path.pop()

        res = []
        if self.root:
            dfs(self.root, [], res)
        return res

    def level_order_traversal(self) -> List[T]:
        pass

    def pre_order_traversal(self) -> List[T]:
        pass

    def is_balanced(self) -> bool:
        pass

    def leaf_similar(self, other: 'Tree') -> bool:
        pass

    def number_of_good_nodes(self) -> int:
        pass

    def path_sum(self, target: T) -> int:
        pass

    def paths_to_target(self, target: T) -> List[T]:
        pass

    def serialize(self) -> str:
        pass
