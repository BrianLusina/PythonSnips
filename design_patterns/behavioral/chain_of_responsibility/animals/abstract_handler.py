from abc import abstractmethod
from typing import Optional, Any

from handler import Handler


class AbstractHandler(Handler):
    """
    Default chaining behaviour can be implemented inside a base handler class
    """
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None
