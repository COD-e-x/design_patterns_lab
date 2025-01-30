from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class BasicNotification(Notification):
    def send(self, message):
        print(f'Отправка SMS: {message}')

# Наследование необходимо, чтобы NotificationDecorator реализовывал интерфейс Notification и мог
# переопределить методы, например, send.
class NotificationDecorator(Notification):
    def __init__(self, notification: Notification):
        self.__notification = notification

    def send(self, message):
        self.__notification.send(message)


class EmailNotificationDecorator(NotificationDecorator):
    def send(self, message: str):

        # Сначала выполним работу метода базового класса
        super().send(message)

        # После добавляем новый функционал для email
        print(f'Отправка E-mail: {message}')

class WhatsAppNotificationDecorator(NotificationDecorator):
    def send(self, message: str):
        # Сначала выполним работу метода базового класса
        super().send(message)
        # После добавляем новый функционал для SMS
        print(f'Отправка WhatsApp сообщение: {message}')


if __name__ == '__main__':
    basic_notification = BasicNotification()

    email_notification = EmailNotificationDecorator(basic_notification)
    whatsapp_email_notification = WhatsAppNotificationDecorator(email_notification)

    # Отправляем уведомление с добавленным функционалом
    whatsapp_email_notification.send('Hello, world!')