from typing import AnyStr, Union, Dict, Optional, Generic, TypeVar, List, Any
from uuid import uuid4
from .edge_type import EdgeType
from .edge import Edge

T = TypeVar("T")


class UndirectedEdge(Edge, Generic[T]):
    """
    Undirected Edge representation of an undirected Edge in a Graph where the edge connects two vertices.
    """

    def __init__(
        self,
        node_one: Any,
        node_two: Any,
        weight: Optional[Union[int, float]] = None,
        properties: Optional[Dict[str, Any]] = None,
        identifier: AnyStr = uuid4(),
    ):
        super().__init__(weight, properties, identifier)
        self.node_one = node_one
        self.node_two = node_two

    def __str__(self):
        return (
            f"{super().__str__()}, NodeOne: {self.node_one}, NodeTwo: {self.node_two}"
        )

    def edge_type(self) -> EdgeType:
        return EdgeType.Undirected

    def vertices(self) -> List[Any]:
        return [self.node_one, self.node_two]
