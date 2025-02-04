from abc import ABC, abstractmethod


class EventListeners(ABC):
    """Абстрактный класс для слушателей событий."""

    @abstractmethod
    def update(self, filename):
        """Метод для обработки события."""
        pass


class EmailAlertsListener(EventListeners):
    """Слушатель для отправки email уведомлений."""

    def update(self, filename):
        print(f'E-mail уведомление: {filename} изменено.')


class LoggingListener(EventListeners):
    """Слушатель для логирования событий."""

    def update(self, filename):
        print(f'Log запись: {filename} обновлена.')


class EventManager:
    """Менеджер для управления подписчиками на события."""

    def __init__(self):
        self.__listeners = {}

    def get_listeners(self):
        """Выводит всех подписчиков."""
        return print({listener for listener in self.__listeners})

    def subscribe(self, event_type, listener):
        """Подписывает слушателя на событие."""
        if event_type not in self.__listeners:
            self.__listeners[event_type] = []
        self.__listeners[event_type].append(listener)

    def unsubscribe(self, event_type, listener):
        """Отписывает слушателя от события."""
        if event_type in self.__listeners:
            self.__listeners[event_type].remove(listener)
            if not self.__listeners[event_type]:
                del self.__listeners[event_type]

    def notify(self, event_type, data):
        """Уведомляет слушателей о событии."""
        for listener in self.__listeners.get(event_type, []):
            listener.update(data)


class Editor:
    """Редактор, который управляет файлами и уведомлениями о событиях."""

    def __init__(self, events: EventManager):
        self.events = events
        self.filename = None

    def open_file(self, filename):
        """Открывает файл и уведомляет слушателей."""
        self.filename = filename
        print(f'Файл {filename} открыт.')
        self.events.notify('open', filename)

    def save_file(self):
        """Сохраняет файл и уведомляет слушателей."""
        if self.filename:
            print(f'Файл {self.filename} сохранен.')
            self.events.notify('save', self.filename)
        else:
            print('Файл не сохранен.')


if __name__ == '__main__':
    event_manager = EventManager()

    email_listener = EmailAlertsListener()
    logging_listener = LoggingListener()

    event_manager.subscribe('open', email_listener)
    event_manager.subscribe('save', logging_listener)

    editor = Editor(event_manager)

    editor.open_file('document.json')
    editor.save_file()

    print()
    EventManager.get_listeners(event_manager)
