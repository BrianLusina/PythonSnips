from typing import Generic, TypeVar, Any, Optional

T = TypeVar("T", bound=Any)


class TreeNode(Generic[T]):
    """
    Tree node class which will implement Tree Node.
    Note that this could be any type of tree node. Not all tree nodes have only left or right children, they could have
    more than one child or more than two children. In this case `children` property is a list of all the immediate
    descendants of the node. This contains the abstract data for each type of tree node that is common for all types
    of nodes
    """

    def __init__(
        self, value: T, key: Optional[Any] = None, parent: Optional["TreeNode"] = None
    ):
        """
        Initialises a tree node with a value, key and a parent node.
        Value here can be anything and the key can be of any type. If not key is provided, then a hash of the data is
        used.
        Args:
            value (T): The value of the node
            key (Optional[Any]): The key of the node. If not provided, a hash of the data is used.
            parent (Optional[TreeNode]): The parent node of the current node.

        Notes:
            The key is used to identify the node in the tree. If not key is provided, a hash of the data is used.
        """
        self.data = value
        self.key = key or hash(value)
        self.parent = parent

    def __repr__(self):
        return f"TreeNode(data={self.data}, key={self.key})"

    def __eq__(self, other: "TreeNode[T]") -> bool:
        """Checks if this node is equal to another node based on the data they contain
        Args:
            other(TreeNode): the other node to compare this node to
        Returns:
            bool: True if this node and the other node are equal, False otherwise
        """
        if other is None:
            return False

        if not isinstance(other, TreeNode):
            return False

        if other.data == self.data:
            return True

        return False

    def __hash__(self):
        return hash(self.data)
