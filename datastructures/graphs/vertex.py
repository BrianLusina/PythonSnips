from typing import Any, Set, Dict, Optional, Generic, TypeVar, List
from .edge import Edge, EdgeType
from uuid import uuid4

T = TypeVar("T")


class Vertex(Generic[T]):
    """
    Graph Node/Vertex representing a Node/Vertex in a Graph
    """

    def __init__(
        self,
        data: T,
        incoming_edges: Set[Edge],
        outgoing_edges: Set[Edge],
        properties: Optional[Dict[str, Any]] = None,
        identifier: Any = uuid4(),
    ):
        self.id = identifier
        self.data = data
        self.incoming_edges = incoming_edges
        self.outgoing_edges = outgoing_edges
        self.edges = self.incoming_edges.union(self.outgoing_edges)
        self.properties = properties

    def __str__(self):
        return (
            f"Id: {self.id}, Data: {self.data}, Properties: {self.properties}, Neighbours: {self.neighbours}. "
            f"Degree: {self.degree}"
        )

    @property
    def neighbours(self) -> List["Vertex"]:
        """Returns a list of all the direct neighbours of this vertex

        Returns:
            List: list of vertices that are direct neighbours or this vertex
        """
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

    @property
    def degree(self) -> int:
        """Number of edges connected to this vertex. This applies to vertices that are in an unweighted graph

        Returns:
            int: Number of edges connected to this vertex
        """
        degrees = 0

        if len(self.incoming_edge) == 0 or len(self.outgoing_edges) == 0:
            return degrees

        seen_edges: Set = {}

        for edge in self.edges:
            if edge not in seen_edges:
                seen_edges.add(edge)
                if not edge.weight:
                    degrees += 1

        return degrees

    @property
    def in_degree(self) -> int:
        """In Degree is the number of directed edges that are incident to this vertex. In other words, point directly
        to this vertex

        Returns:
            int: number of directed edges or incoming edges
        """
        in_degrees = 0
        if len(self.edges) == 0:
            return in_degrees

        for edge in self.edges:
            if edge.type == EdgeType.DIRECTED and edge.destination == self:
                in_degrees += 1

        return in_degrees

    @property
    def out_degree(self) -> int:
        """Out Degree is the number of directed edges that are incident to this vertex. In other words, point directly
        from this vertex where this vertex is the source

        Returns:
            int: number of directed edges or outgoing edges
        """
        out_degrees = 0
        if len(self.edges) == 0:
            return out_degrees

        for edge in self.edges:
            if edge.type == EdgeType.DIRECTED and edge.source == self:
                out_degrees += 1

        return out_degrees

    def add_adjacent_vertex(self, other: "Vertex"):
        """Adds an adjacent vertex to the list of neighbors. Note that this is useful in a graph as the graph will be
        able the call this method on this vertex & the same method on the other vertex showing undirected relationship.

        Args:
            other (Vertex): Vertex to add as a neighbor
        """

    def __eq__(self, other: "Vertex") -> bool:
        return self.id == other.id
