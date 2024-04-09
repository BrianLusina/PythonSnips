from typing import List

from datastructures.trees import TreeNode, T


class TernaryTreeNode(TreeNode):
    """
    Ternary tree node class which represents a node in a Ternary tree
    """

    def __init__(self, data: T, children: List["TernaryTreeNode"] = []):
        """
        InitializesValue here can be anything
        """
        super().__init__(data)
        self._children = children

    def clear_node(self):
        """
        Clears the node and sets the datas to None
        """
        self._children = []

    @property
    def children(self) -> List["TernaryTreeNode"]:
        return self._children

    def __repr__(self):
        return f"TernaryTreeNode(data={self.data}, children={self._children})"

    def __eq__(self, other: "TernaryTreeNode") -> bool:
        """Checks if this node is equal to another node based on the data they contain
        Args:
            other(TernaryTreeNode): the other node to compare this node to
        Returns:
            bool: True if this node and the other node are equal, False otherwise
        """
        if other is None:
            return False

        if other.data == self.data:
            return True

        return False
