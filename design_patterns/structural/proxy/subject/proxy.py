from subject import Subject
from real_subject import RealSubject


class Proxy(Subject):
    """
    The Proxy has an interface identical to the RealSubject.
    """

    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    @staticmethod
    def check_access() -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    @staticmethod
    def log_access() -> None:
        print("Proxy: Logging time of request")
