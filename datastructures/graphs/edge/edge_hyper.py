from typing import AnyStr, Union, Dict, Optional, Generic, TypeVar, List, Any
from uuid import uuid4
from .edge_type import EdgeType
from .edge import Edge

T = TypeVar("T")


class HyperEdge(Edge, Generic[T]):
    """
    HyperEdge representation of a hyper-edge in a Graph where the edge connects to the multiple vertices
    """

    def __init__(
        self,
        nodes: List[Any],
        weight: Optional[Union[int, float]] = None,
        properties: Optional[Dict[str, Any]] = None,
        identifier: AnyStr = uuid4(),
    ):
        super().__init__(weight, properties, identifier)
        self.nodes = nodes

    def __str__(self):
        return f"{super().__str__()}, Nodes: {self.nodes}"

    def edge_type(self) -> EdgeType:
        return EdgeType.SELF

    def vertices(self) -> List[Any]:
        return self.nodes
