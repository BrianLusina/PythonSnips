from design_patterns.creational.factory.notification.email_notification import (
    EmailNotification,
)
from design_patterns.creational.factory.notification import Notification
from design_patterns.creational.factory.notification.sms_notification import (
    SmsNotification,
)


class NotificationFactory:
    @staticmethod
    def create(self, notification_type: str) -> Notification:
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SmsNotification()
        raise ValueError("Invalid notification type")
