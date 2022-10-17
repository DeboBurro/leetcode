# REF: https://leetcode.com/discuss/interview-question/object-oriented-design/2312435/Amazon-or-LLD-Notification-system
# Design system for sending different typr of messages : Email, SMS, What
from enum import Enum, auto
from typing import Dict
from abc import ABC, abstractmethod


class NotificationType(Enum):
    EMAIL = auto()
    SMS = auto()
    WHATSAPP = auto()

########## notifications #####################
# The id should be fetched from another service RPC call 
class Notification(ABC):
    def __init__(self, id: int, notification_type: NotificationType) -> None:
        self.id: int = id
        self.notification_type: NotificationType = notification_type


class EmailNotification(Notification):
    def __init__(self, id: int, fromEmail: str, toEmail: str, subject: str) -> None:
        self.notification_type: NotificationType = NotificationType.EMAIL
        self.id = id
        self.fromEmail = fromEmail
        self.toEmail = toEmail
        self.subject = subject

class SmsNotification(Notification):
    def __init__(self, id:int, toNumber: str, body: str) -> None:
        self.notification_type = NotificationType.SMS
        self.id = id
        self.toNumber = toNumber
        self.body = body

class WhatsappNotification(Notification):
    def __init__(self, id:int, toNumber: str, body: str) -> None:
        self.notification_type = NotificationType.WHATSAPP
        self.id = id
        self.toNumber = toNumber
        self.body = body

##########  notification handler  ############
class NotificationHandler(ABC):
    @abstractmethod
    def send_notification(notification: Notification) -> None:
        raise NotImplementedError('Please implemtn send_notification function')

class EmailNotificationHandler(NotificationHandler):
    @staticmethod
    def send_notification(email_notification: EmailNotification) -> None:
        # logic of sending email notification 
        print(f'Email is sent, id: {email_notification.id}, from: {email_notification.fromEmail}, to: {email_notification.toEmail}, subject: {email_notification.subject}, notification_type: {email_notification.notification_type}')
        pass

class SmsNotificationHandler(NotificationHandler):
    @staticmethod
    def send_notification(sms_notification: SmsNotification) -> None:
        # logic of sending sms notification 
        pass

class WhatsappNotificationHandler(NotificationHandler):
    @staticmethod
    def send_notification(whatsapp_notification: WhatsappNotification) -> None:
        # logic of sending whatsapp notification 
        pass

##########  Notification Factory  ############

class NotificationHandlerFactory:
    handlers: Dict[NotificationType, NotificationHandler] = {}
    handlers[NotificationType.EMAIL] = EmailNotificationHandler()
    handlers[NotificationType.SMS] = SmsNotificationHandler()
    handlers[NotificationType.WHATSAPP] = WhatsappNotificationHandler()
    
    @staticmethod
    def get_notification_handler(NotificationType):
        return NotificationHandlerFactory.handlers.get(NotificationType)
    
############  Notification Service     ######################
class NotificationService:
    notification_handler_factory = NotificationHandlerFactory



if __name__ == '__main__':
    # use case example: 
    notification_handler_factory = NotificationService.notification_handler_factory
    email_notificaton_handler = notification_handler_factory.get_notification_handler(NotificationType.EMAIL)
    email_notification = EmailNotification(123, 'abc@gmail.com', 'cde@gamil.com', 'suject title')
    email_notificaton_handler.send_notification(email_notification)