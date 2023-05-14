from queue import Full


class QueueFullException(Full):
    """Queue full exception thrown when a queue is full"""


class QueueEmptyException(Exception):
    """Queue Empty exception raised when a queue is empty"""
