from abc import ABC, abstractmethod


class Context:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    """
    A reference to the current state of the Context.
    """
    _state = None

    def __init__(self, state) -> None:
        self.transition_to(state)

    def transition_to(self, state):
        """
        The Context allows changing the State object at runtime.
        @param state: State to transition to
        """
        self._state = state
        self._state.context = self

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, ctx: Context) -> None:
        self._context = ctx

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1")
        print("ConcreteStateA wants to change state of context")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2")


class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2")
        print("ConcreteStateB wants to change state of context")
        self.context.transition_to(ConcreteStateA())


if __name__ == "__main__":
    context = Context(ConcreteStateA())
    context.request1()
    context.request2()
