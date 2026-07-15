from typing import List, Dict, Optional
from datetime import datetime, UTC
from design_patterns.event_stream.event import Event
import logging


class AuditLogger:
    """Logs all events for audit purposes, even those not consumed"""

    def __init__(self):
        self.audit_log: List[Dict] = []

    def log_event(
        self, event: Event, message_id: str, handled: bool, reason: Optional[str] = None
    ):
        """Log event with handling status"""
        log_entry = {
            "timestamp": datetime.now(UTC).isoformat(),
            "event_type": event.event_type.value,
            "message_id": message_id,
            "event_timestamp": event.timestamp.isoformat(),
            "source": event.source,
            "handled": handled,
            "reason": reason,
            "metadata": event.metadata,
        }
        self.audit_log.append(log_entry)

        # Also log to standard logger
        log_level = logging.INFO if handled else logging.WARNING
        logging.log(
            log_level,
            f"Event {event.event_type.value} for message {message_id}: "
            f"{'Handled' if handled else f'Skipped - {reason}'}",
        )

    def get_audit_trail(self, message_id: Optional[str] = None) -> List[Dict]:
        """Retrieve audit logs, optionally filtered by message_id"""
        if message_id:
            return [log for log in self.audit_log if log["message_id"] == message_id]
        return self.audit_log
