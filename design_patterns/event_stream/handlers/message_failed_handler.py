from typing import Optional
from design_patterns.event_stream.message_context import MessageContext as Message
from design_patterns.event_stream.message_state import MessageState
from design_patterns.event_stream.event import Event
from design_patterns.event_stream.event_type import EventType
from design_patterns.event_stream.handlers.event_handler import EventHandler
from design_patterns.event_stream.state_transition_config import StateTransitionConfig
import logging


class MessageFailedHandler(EventHandler):
    """Handles MESSAGE_FAILED events"""

    def can_handle(self, event: Event) -> bool:
        return event.event_type == EventType.MESSAGE_FAILED

    def get_target_state(self, event: Event) -> Optional[MessageState]:
        return MessageState.FAILED

    def handle(self, event: Event, message: Message) -> bool:
        target_state = self.get_target_state(event)
        if StateTransitionConfig.is_valid_transition(
            message.current_state, target_state
        ):
            message.transition_to(target_state, event.timestamp)
            failure_reason = event.metadata.get("reason", "Unknown")
            logging.error(f"Message {message.message_id} failed: {failure_reason}")
            return True
        return False
