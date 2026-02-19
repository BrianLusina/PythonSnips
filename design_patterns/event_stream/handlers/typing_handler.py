from typing import Optional
from design_patterns.event_stream.message_context import MessageContext
from design_patterns.event_stream.message_state import MessageState
from design_patterns.event_stream.event import Event
from design_patterns.event_stream.event_type import EventType
from design_patterns.event_stream.handlers.event_handler import EventHandler
import logging


class TypingEventHandler(EventHandler):
    """Handles IS_TYPING and TYPING_STOPPED events"""

    def can_handle(self, event: Event) -> bool:
        return event.event_type in {EventType.IS_TYPING, EventType.TYPING_STOPPED}

    def get_target_state(self, event: Event) -> Optional[MessageState]:
        if event.event_type == EventType.IS_TYPING:
            return MessageState.COMPOSING
        return None  # TYPING_STOPPED doesn't change state

    def handle(self, event: Event, message: MessageContext) -> bool:
        if event.event_type == EventType.IS_TYPING:
            # Only transition to composing if we're not already past that state
            if message.current_state == MessageState.COMPOSING:
                logging.info(f"User typing for message {message.message_id}")
                return True
        return False
