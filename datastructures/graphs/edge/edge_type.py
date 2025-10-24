from enum import Enum, unique


@unique
class EdgeType(Enum):
    UNDIRECTED = 1
    DIRECTED = 2
    SELF = 3
    HYPER_DIRECTED = 4
    HYPER_UNDIRECTED = 5
