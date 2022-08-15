from typing import Any, AnyStr, Set, Dict, Optional
from .edge import Edge
from uuid import uuid4


class Vertex(object):
    """
    Graph Node/Vertex representing a Node/Vertex in a Graph
    """

    def __init__(self, data: Any, incoming_edges: Set[Edge], outgoing_edges: Set[Edge],
                 properties: Optional[Dict[str, Any]] = None, identifier: AnyStr = uuid4()):
        self.id = identifier
        self.data = data
        self.incoming_edges = incoming_edges
        self.outgoing_edges = outgoing_edges
        self.properties = properties

    def __str__(self):
        return f"Id: {self.id}, Data: {self.data}, Properties: {self.properties}, Neighbours: {self.neighbours}"

    @property
    def neighbours(self):
        nodes = []
        for edge in self.incoming_edges:
            node = edge.source
            if node.id != self.id:
                nodes.append(node)
            nodes.append(node)

        for edge in self.outgoing_edges:
            node = edge.destination
            if node.id != self.id:
                nodes.append(node)

        return nodes
