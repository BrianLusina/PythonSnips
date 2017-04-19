class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, size):
        self.buffer = bytearray(size)
        self.read_point = 0
        self.write_point = 0

    def _update_buffer(self, data):
        """
        Protected helper method for Python 2/3
        """
        try:
            self.buffer[self.write_point] = data
        except TypeError:
            self.buffer[self.write_point] = ord(data)

    def clear(self):
        self.buffer = bytearray(len(self.buffer))

    def write(self, data):
        if all(self.buffer):
            raise BufferFullException
        self._update_buffer(data)
        self.write_point = (self.write_point + 1) % len(self.buffer)

    def read(self):
        if not any(self.buffer):
            raise BufferEmptyException
        data = chr(self.buffer[self.read_point])
        self.buffer[self.read_point] = 0
        self.read_point = (self.read_point + 1) % len(self.buffer)
        return data

    def overwrite(self, data):
        self._update_buffer(data)
        if all(self.buffer) and self.read_point == self.write_point:
            self.read_point = (self.read_point + 1) % len(self.buffer)
        self.write_point = (self.write_point + 1) % len(self.buffer)
