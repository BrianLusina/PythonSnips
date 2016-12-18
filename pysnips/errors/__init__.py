class PySnipsError(Exception):
    """
    My own exception class
    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg

    @staticmethod
    def __new__(*args, **kwargs):
        return super().__new__(*args, **kwargs)

