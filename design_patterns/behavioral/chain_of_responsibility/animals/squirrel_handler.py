from typing import Any, Optional

from abstract_handler import AbstractHandler


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        return super().handle(request)
