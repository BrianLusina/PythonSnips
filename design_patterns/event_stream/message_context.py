from typing import Dict, Any, List, Tuple
from dataclasses import dataclass, field
from datetime import datetime, UTC
from design_patterns.event_stream.message_state import MessageState


@dataclass
class MessageContext:
    """
    A lightweight DTO (Data Transfer Object) to pass around.
    """

    message_id: str
    sender_id: str
    recipient_id: str
    content: str
    timestamp: str
    raw_payload: Dict[str, Any]
    current_state: MessageState = MessageState.COMPOSING
    state_history: List[Tuple[MessageState, datetime]] = field(
        default_factory=list
    )  # (state, timestamp)
    created_at: datetime = field(default_factory=datetime.now)

    def transition_to(self, new_state: MessageState, timestamp: datetime = None):
        """Record state transition"""
        timestamp = timestamp or datetime.now(UTC)
        self.state_history.append((self.current_state, timestamp))
        self.current_state = new_state
