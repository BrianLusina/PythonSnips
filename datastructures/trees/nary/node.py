from datastructures.trees.node import TreeNode, T


class NAryNode(TreeNode):
    def __init__(self, value: T, children=None):
        super().__init__(value)
        if children is None:
            children = []
        self.children = children

    def __repr__(self):
        return f"{super().__repr__()} children: {self.children})"
