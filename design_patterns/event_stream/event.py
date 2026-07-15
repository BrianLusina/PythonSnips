from dataclasses import dataclass, field
from typing import Dict, Any
from datetime import datetime
from design_patterns.event_stream.event_type import EventType


@dataclass
class Event:
    """Represents an incoming event from external APIs"""

    event_type: EventType
    message_id: str
    timestamp: datetime
    metadata: Dict[str, Any] = field(default_factory=dict)
    source: str = "google_rcs"  # Which API the event came from
