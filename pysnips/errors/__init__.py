class PySnipsError(Exception):
    """
    My own exception class
    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, name, msg):
        self.name = name
        self.msg = msg

