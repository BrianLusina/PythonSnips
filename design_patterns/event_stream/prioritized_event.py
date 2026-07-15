from dataclasses import dataclass, field
from datetime import datetime
from design_patterns.event_stream.event import Event


@dataclass(order=True)
class PrioritizedEvent:
    """Event wrapper for priority queue processing"""

    priority: int  # Lower number = higher priority
    timestamp: datetime = field(compare=True)
    event: Event = field(compare=False, default=None)
