from typing import Dict, List, Callable, Optional
import logging
from datetime import datetime, UTC
from collections import defaultdict
from design_patterns.event_stream.message_context import MessageContext as Message
from design_patterns.event_stream.event import Event
from design_patterns.event_stream.event_type import EventType
from design_patterns.event_stream.message_state import MessageState
from design_patterns.event_stream.audit_logger import AuditLogger
from design_patterns.event_stream.handlers import (
    EventHandler,
    TypingEventHandler,
    MessageRevokedHandler,
    MessageSentHandler,
    MessageReadHandler,
    MessageFailedHandler,
    MessageDeliveredHandler,
)


class MessageStateManager:
    """
    Central orchestrator for message state management.
    Uses a handler chain pattern for efficient event processing.
    """

    def __init__(self):
        # Message storage: O(1) lookup by message_id
        self.messages: Dict[str, Message] = {}

        # Handler chain: handlers are checked in order
        self.handlers: List[EventHandler] = [
            TypingEventHandler(),
            MessageSentHandler(),
            MessageDeliveredHandler(),
            MessageReadHandler(),
            MessageFailedHandler(),
            MessageRevokedHandler(),
        ]

        # Map event types to handlers for O(1) lookup
        self.event_handler_map: Dict[EventType, EventHandler] = {}
        self._build_event_handler_map()

        # Audit logger
        self.audit_logger = AuditLogger()

        # Callbacks for state changes (Observer pattern)
        self.state_change_callbacks: Dict[MessageState, List[Callable]] = defaultdict(
            list
        )

    def _build_event_handler_map(self):
        """Build efficient event type to handler mapping"""
        for handler in self.handlers:
            # This is a simple approach; for production, you might want
            # to make handlers declare their event types explicitly
            for event_type in EventType:
                dummy_event = Event(event_type, "", datetime.now(UTC))
                if handler.can_handle(dummy_event):
                    self.event_handler_map[event_type] = handler

    def register_message(self, message: Message):
        """Register a new message in the system"""
        self.messages[message.message_id] = message
        logging.info(f"Registered message {message.message_id}")

    def register_state_callback(self, state: MessageState, callback: Callable):
        """Register a callback to be invoked when a message reaches a state"""
        self.state_change_callbacks[state].append(callback)

    def process_event(self, event: Event) -> bool:
        """
        Process an incoming event.
        Returns True if event was handled, False if skipped.
        """
        message_id = event.message_id

        # Get or create message
        message = self.messages.get(message_id)
        if not message:
            # For now, log and skip events for unknown messages
            self.audit_logger.log_event(
                event, message_id, False, "Message not found in system"
            )
            return False

        # Find appropriate handler using O(1) map lookup
        handler = self.event_handler_map.get(event.event_type)

        if not handler:
            # Event type not recognized - log for audit
            self.audit_logger.log_event(
                event,
                message_id,
                False,
                f"No handler for event type {event.event_type.value}",
            )
            return False

        # Store previous state for callback comparison
        previous_state = message.current_state

        # Attempt to handle the event
        handled = handler.handle(event, message)

        # Log to audit trail
        reason = None if handled else "Invalid state transition or event ignored"
        self.audit_logger.log_event(event, message_id, handled, reason)

        # Invoke state change callbacks if state changed
        if handled and message.current_state != previous_state:
            self._invoke_state_callbacks(message, previous_state)

        return handled

    def _invoke_state_callbacks(self, message: Message, previous_state: MessageState):
        """Invoke registered callbacks for state transitions"""
        callbacks = self.state_change_callbacks.get(message.current_state, [])
        for callback in callbacks:
            try:
                callback(message, previous_state)
            except Exception as e:
                logging.error(f"Callback error for message {message.message_id}: {e}")

    def get_message_state(self, message_id: str) -> Optional[MessageState]:
        """Get current state of a message"""
        message = self.messages.get(message_id)
        return message.current_state if message else None

    def get_message_history(self, message_id: str) -> List[tuple]:
        """Get state transition history for a message"""
        message = self.messages.get(message_id)
        return message.state_history if message else []

    def get_audit_trail(self, message_id: Optional[str] = None) -> List[Dict]:
        """Get audit trail for all or specific message"""
        return self.audit_logger.get_audit_trail(message_id)
