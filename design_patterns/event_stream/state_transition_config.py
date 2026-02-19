from typing import Dict, Set
from design_patterns.event_stream.message_state import MessageState


class StateTransitionConfig:
    """
    Defines valid state transitions using an adjacency list for O(1) lookup.
    This ensures we only allow valid state transitions.
    """

    # Valid transitions represented as a directed graph
    VALID_TRANSITIONS: Dict[MessageState, Set[MessageState]] = {
        MessageState.COMPOSING: {
            MessageState.SENT,
            MessageState.FAILED,
        },
        MessageState.SENT: {
            MessageState.DELIVERED,
            MessageState.FAILED,
            MessageState.REVOKED,
        },
        MessageState.DELIVERED: {
            MessageState.READ,
            MessageState.REVOKED,
        },
        MessageState.READ: {
            MessageState.REVOKED,
        },
        MessageState.FAILED: set(),  # Terminal state
        MessageState.REVOKED: set(),  # Terminal state
    }

    @classmethod
    def is_valid_transition(
        cls, from_state: MessageState, to_state: MessageState
    ) -> bool:
        """Check if transition is valid in O(1) time"""
        return to_state in cls.VALID_TRANSITIONS.get(from_state, set())
