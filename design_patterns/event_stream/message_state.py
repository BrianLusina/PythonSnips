from enum import Enum, auto


class MessageState(Enum):
    """Enum representing all possible message states"""

    COMPOSING = auto()  # User is typing
    SENT = auto()  # Message sent from sender
    DELIVERED = auto()  # Message delivered to recipient device
    READ = auto()  # Message read by recipient
    FAILED = auto()  # Message failed to send
    REVOKED = auto()  # Message revoked/deleted
