import asyncio
from design_patterns.event_stream.message_context import MessageContext
from design_patterns.event_stream.logger import logger


async def handle_typing(ctx: MessageContext):
    """
    Transient State: Doesn't persist to DB, just notifies the socket.
    """
    # Simulate an external API call to a WebSocket server
    logger.info(
        f"⚡ [Realtime] User {ctx.sender_id} is typing on msg {ctx.message_id}..."
    )
    await asyncio.sleep(0.01)  # Simulate network I/O


async def handle_delivered(ctx: MessageContext):
    """
    Persistent State: Updates DB to 'DELIVERED'.
    """
    logger.info(f"💾 [DB Write] Message {ctx.message_id} marked as DELIVERED.")
    # SQL: UPDATE messages SET status='DELIVERED' WHERE id=...
    await asyncio.sleep(0.05)


async def handle_read(ctx: MessageContext):
    """
    Persistent State: Updates DB to 'READ'.
    """
    logger.info(f"💾 [DB Write] Message {ctx.message_id} marked as READ.")
    logger.info(f"🔔 [Notify] Sender informed that message {ctx.message_id} was read.")
    await asyncio.sleep(0.05)


async def handle_inbound(ctx: MessageContext):
    """
    New Message: Creates a new record.
    """
    logger.info(f"📨 [New Msg] Processing inbound content for {ctx.message_id}.")
