from typing import Dict, Callable, Awaitable, Any
from design_patterns.event_stream.event_type import EventType
from design_patterns.event_stream.message_context import MessageContext
from design_patterns.event_stream.handlers.handlers import (
    handle_typing,
    handle_read,
    handle_delivered,
    handle_inbound,
)
from design_patterns.event_stream.logger import logger


class EventProcessor:
    def __init__(self):
        # The Dispatch Table: O(1) Lookup
        # We map the Enum directly to the function reference.
        self._handlers: Dict[EventType, Callable[[MessageContext], Awaitable[None]]] = {
            EventType.IS_TYPING: handle_typing,
            EventType.DELIVERED: handle_delivered,
            EventType.READ: handle_read,
            EventType.INBOUND_MESSAGE: handle_inbound,
        }

    async def _audit_log(self, raw_payload: dict, processed: bool):
        """
        Audit logging happens for EVERY event, consumed or not.
        Using asyncio.create_task ensures this doesn't block the response.
        """
        status = "PROCESSED" if processed else "IGNORED"
        # In production, send this to Elasticsearch/DataDog/S3
        logger.debug(f"📝 [AUDIT - {status}] Payload: {raw_payload}")

    async def process_event(self, raw_payload: Dict[str, str]):
        """
        Main entry point.
        """
        # 1. Parse Event Type safely
        event_str = raw_payload.get("event_type")

        try:
            event_type = EventType(event_str)
        except ValueError:
            # Event type not in our Enum -> It is an event we skip (but still audit)
            await self._audit_log(raw_payload, processed=False)
            return

        # 2. Extract Context (Fast parsing)
        ctx = MessageContext(
            message_id=raw_payload.get("messageId"),
            sender_id=raw_payload.get("senderId"),
            timestamp=raw_payload.get("timestamp"),
            raw_payload=raw_payload,
        )

        # 3. Dispatch
        handler = self._handlers.get(event_type)

        if handler:
            # Fire off the specific logic
            await handler(ctx)
            await self._audit_log(raw_payload, processed=True)
        else:
            # Should technically be caught by the try/except, but good as a fallback
            await self._audit_log(raw_payload, processed=False)
