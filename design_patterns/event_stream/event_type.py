from enum import Enum


class EventType(Enum):
    """
    Enum for O(1) comparison speed and type safety.
    Matches the event strings coming from the external API.
    """

    IS_TYPING = "IS_TYPING"
    DELIVERED = "DELIVERED"
    READ = "READ"
    INBOUND_MESSAGE = "INBOUND_MESSAGE"
    FAILED = "FAILED"
    MESSAGE_FAILED = "MESSAGE_FAILED"
    MESSAGE_REVOKED = "MESSAGE_REVOKED"
    MESSAGE_READ = "MESSAGE_READ"
    MESSAGE_DELIVERED = "MESSAGE_DELIVERED"
    MESSAGE_SENT = "MESSAGE_SENT"
    TYPING_STOPPED = "TYPING_STOPPED"
