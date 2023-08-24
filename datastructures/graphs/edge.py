from typing import AnyStr, Optional, Union, Dict, Any
from enum import Enum, unique
from uuid import uuid4
from .node import Vertex


@unique
class EdgeType(Enum):
    UNDIRECTED = 1
    DIRECTED = 2
    SELF_DIRECTED = 3
    SELF_UNDIRECTED = 4
    HYPER_DIRECTED = 5
    HYPER_UNDIRECTED = 6


class Edge:
    """
    Edge representation of an Edge in a Graph
    """

    def __init__(self, source: Vertex, destination: Vertex, weight: Optional[Union[int, float]] = None,
                 edge_type: EdgeType = EdgeType.UNDIRECTED,
                 relationship_type: Optional[AnyStr] = None,
                 properties: Optional[Dict[str, Any]] = None,
                 identifier: AnyStr = uuid4()):
        self.id = identifier
        self.source = source
        self.destination = destination
        self.weight = weight
        self.type = edge_type
        self.properties = properties
        self.relationship_type = relationship_type

        self.__validate_edge()

    def __validate_edge(self):
        if self.type == EdgeType.SELF_DIRECTED or self.type == EdgeType.SELF_UNDIRECTED:
            if self.destination.id != self.source.id:
                raise ValueError(
                    f"Edge denoted as {self.type} but source node {self.source} & "
                    f"destination node {self.destination} are not the same")

    def __str__(self):
        return f"Id: {self.id}, Source: {self.source}, Destination: {self.destination}, Weight: {self.weight}, " \
               f"Properties: {self.properties}, RelationshipType: {self.relationship_type}"
