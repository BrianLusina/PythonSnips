import asyncio
from design_patterns.event_stream.processor import EventProcessor


async def main():
    event_processor = EventProcessor()

    # Incoming stream of events from Google/RCS
    events_stream = [
        {
            "event_type": "IS_TYPING",
            "messageId": "msg_123",
            "senderId": "user_A",
            "timestamp": "10:00:01",
        },
        {
            "event_type": "INBOUND_MESSAGE",
            "messageId": "msg_123",
            "senderId": "user_A",
            "timestamp": "10:00:05",
        },
        # An event we don't care about (e.g., BATTERY_LOW)
        {
            "event_type": "USER_BATTERY_LOW",
            "messageId": "msg_123",
            "senderId": "user_A",
            "timestamp": "10:00:06",
        },
        {
            "event_type": "DELIVERED",
            "messageId": "msg_123",
            "senderId": "user_A",
            "timestamp": "10:00:07",
        },
        {
            "event_type": "READ",
            "messageId": "msg_123",
            "senderId": "user_A",
            "timestamp": "10:00:15",
        },
    ]

    print("--- Starting Event Stream Processing ---")

    # Process them concurrently
    tasks = [event_processor.process_event(event) for event in events_stream]
    await asyncio.gather(*tasks)

    print("--- Stream Finished ---")


if __name__ == "__main__":
    asyncio.run(main())
