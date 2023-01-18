from abc import ABC, abstractmethod


class Memento(ABC):
    """
    Memento interface provides a way to retrieve the memento's metadata such as creation date or name. However, it does
    not expose the originator's state.
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass
