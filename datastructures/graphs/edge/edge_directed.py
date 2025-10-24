from typing import AnyStr, Union, Dict, Optional, Generic, TypeVar, List, Any
from uuid import uuid4
from .edge_type import EdgeType
from .edge import Edge

T = TypeVar("T")

class DirectedEdge(Edge, Generic[T]):
    """
    Directed Edge representation of a directed Edge in a Graph where the edge connects two vertices which has a source
    vertex and a destination vertex.
    """

    def __init__(self, source: Any, destination: Any, weight: Optional[Union[int, float]] = None,
                 properties: Optional[Dict[str, Any]] = None,
                 identifier: AnyStr = uuid4()):
        super().__init__(weight, properties, identifier)
        self.source = source
        self.destination = destination

    def __str__(self):
        return f"{super().__str__()}, Source: {self.source}, Destination: {self.destination}"

    def edge_type(self) -> EdgeType:
        return EdgeType.DIRECTED

    def vertices(self) -> List[Any]:
        return [self.source, self.destination]
