from design_patterns.creational.factory.notification import Notification


class EmailNotification(Notification):
    def send(self, message: str) -> None:
        pass
