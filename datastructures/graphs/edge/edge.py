from abc import ABC, abstractmethod
from typing import AnyStr, Union
from .edge_type import EdgeType
from typing import Any, Dict, Optional, Generic, TypeVar, List
from uuid import uuid4

T = TypeVar("T")

class Edge(ABC, Generic[T]):
    """
    Edge representation of an abstract Edge in a Graph
    """

    def __init__(
        self,
        weight: Optional[Union[int, float]] = None,
        properties: Optional[Dict[str, Any]] = None,
        identifier: AnyStr = uuid4(),
    ):
        self.id = identifier
        self.weight = weight
        self.properties = properties

    def __str__(self):
        return f"Id: {self.id}, Weight: {self.weight}, Properties: {self.properties}"

    @abstractmethod
    def edge_type(self) -> EdgeType:
        raise NotImplementedError("Not implemented")

    def is_unweighted(self) -> bool:
        return self.weight is None

    @abstractmethod
    def vertices(self) -> List[Any]:
        raise NotImplementedError("Not implemented")
