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
        identifier: Any = uuid4(),
        properties: Optional[Dict[str, Any]] = None,
        incoming_edges: Optional[Set[Edge]] = None,
        outgoing_edges: Optional[Set[Edge]] = None,
    ):
        if outgoing_edges is None:
            outgoing_edges = set()
        if incoming_edges is None:
            incoming_edges = set()
        self.id = identifier
        self.data = data
        self.incoming_edges = incoming_edges
        self.outgoing_edges = outgoing_edges
        self.edges = self.incoming_edges.union(self.outgoing_edges)
        self.adjacent_vertices: Dict[str, 'Vertex'] = {}
        self.properties = properties

    def __str__(self):
        return (
            f"Id: {self.id}, Data: {self.data}, Properties: {self.properties}, Neighbours: {self.neighbours}. "
            f"Degree: {self.degree}"
        )

    def __eq__(self, other: "Vertex") -> bool:
        return self.id == other.id

    def add_adjacent_vertex(self, other: "Vertex") -> None:
        """Adds an adjacent vertex to the list of neighbors. Note that this is useful in a graph as the graph will be
        able the call this method on this vertex and the same method on the other vertex showing undirected relationship.

        Args:
            other (Vertex): Vertex to add as a neighbor
        """
        # should not be able to add self as an adjacent vertex
        if other is self or other.id == self.id:
            return

        # only add adjacent vertex if not already present.
        if not self.adjacent_vertices.get(other.id):
            self.adjacent_vertices[other.id] = other
            other.add_adjacent_vertex(self)

    @property
    def neighbours(self) -> List["Vertex"]:
        """Returns a list of all the direct neighbors of this vertex

        Returns:
            List: list of vertices that are direct neighbors or this vertex
        """
        nodes = []
        for vertex in self.adjacent_vertices.values():
            nodes.append(vertex)

        return nodes

    @property
    def degree(self) -> int:
        """Number of edges connected to this vertex. This applies to vertices that are in an unweighted graph

        Returns:
            int: Number of edges connected to this vertex
        """
        degrees = 0

        if len(self.incoming_edges) == 0 or len(self.outgoing_edges) == 0:
            return degrees

        seen_edges: Set = set()

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
            if edge.type == EdgeType.DIRECTED and edge.node_two == self:
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
            if edge.type == EdgeType.DIRECTED and edge.node_one == self:
                out_degrees += 1

        return out_degrees

