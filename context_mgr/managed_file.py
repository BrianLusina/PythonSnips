from contextlib import contextmanager


@contextmanager
def managed_file(name):
    """
    Managed file context manager approach using a generator
    This uses the contexmanager decorator to create a context manager that manages files
    the try...finally block acquires the resource and yields the resource for use with the caller
    Once the caller leaves the with statement, the finally block is executed, allowing the resources
    to be returned to the system
    """
    try:
        f = open(name, "w")
        yield f

    finally:
        f.close()


class ManagedFile(object):
    """
    Managed file class that opens a file in write mode. this follows the context manager protocol
    by implementing the __enter__ and __exit__ methods
    """

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


if __name__ == "__main__":
    with ManagedFile("hello.txt") as f:
        f.write("Hello,world")
        f.write("Bye Now")

    with managed_file("hello.txt") as f:
        f.write("writing from custom context manager with decorator")
        f.write("alrigh,bye")
