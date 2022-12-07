from typing import Any, Optional

from abstract_handler import AbstractHandler


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        return super().handle(request)
