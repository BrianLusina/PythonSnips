from typing import Dict
from design_patterns.event_stream.event_type import EventType


class EventPriorityMapper:
    """Maps event types to processing priorities"""

    PRIORITY_MAP: Dict[EventType, int] = {
        EventType.MESSAGE_FAILED: 1,  # Highest priority
        EventType.MESSAGE_REVOKED: 1,
        EventType.MESSAGE_READ: 2,
        EventType.MESSAGE_DELIVERED: 3,
        EventType.MESSAGE_SENT: 4,
        EventType.IS_TYPING: 5,  # Lowest priority
        EventType.TYPING_STOPPED: 5,
    }

    @classmethod
    def get_priority(cls, event_type: EventType) -> int:
        """Get priority for event type"""
        return cls.PRIORITY_MAP.get(event_type, 10)
