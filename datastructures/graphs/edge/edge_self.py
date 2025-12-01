from typing import AnyStr, Union, Dict, Optional, Generic, TypeVar, List, Any
from uuid import uuid4
from .edge_type import EdgeType
from .edge import Edge

T = TypeVar("T")


class SelfEdge(Edge, Generic[T]):
    """
    Self-Edge representation of a self-edge in a Graph where the edge connects to the same vertex
    """

    def __init__(
        self,
        node: Any,
        weight: Optional[Union[int, float]] = None,
        properties: Optional[Dict[str, Any]] = None,
        identifier: AnyStr = uuid4(),
    ):
        super().__init__(weight, properties, identifier)
        self.node_one = node

    def __str__(self):
        return f"{super().__str__()}, Node: {self.node_one}"

    def edge_type(self) -> EdgeType:
        return EdgeType.SELF

    def vertices(self) -> List[Any]:
        return [self.node_one]
