from design_patterns.creational.factory.notification import Notification


class SmsNotification(Notification):
    def send(self, message: str) -> None:
        pass
