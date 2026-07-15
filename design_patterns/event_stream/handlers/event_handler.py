from abc import ABC, abstractmethod
from typing import Optional
from design_patterns.event_stream.event import Event
from design_patterns.event_stream.message_state import MessageState
from design_patterns.event_stream.message_context import MessageContext

# ============================================================================
# EVENT HANDLERS (Strategy Pattern)
# ============================================================================


class EventHandler(ABC):
    """Abstract base class for event handlers"""

    @abstractmethod
    def can_handle(self, event: Event) -> bool:
        """Determine if this handler can process the event"""
        pass

    @abstractmethod
    def handle(self, event: Event, message: MessageContext) -> bool:
        """
        Process the event and update message state.
        Returns True if handled successfully, False otherwise.
        """
        pass

    @abstractmethod
    def get_target_state(self, event: Event) -> Optional[MessageState]:
        """Get the target state for this event type"""
        pass
