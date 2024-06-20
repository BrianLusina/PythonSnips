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

    def __init__(self, value: T, key: Optional[Any] = None):
        """
        Value here can be anything and the key can be of any type. If not key is provided, then a hash of the data is
        used.
        """
        self.data = value
        self.key = key or hash(value)

    def __repr__(self):
        return f"TreeNode(data={self.data}, key={self.key})"
