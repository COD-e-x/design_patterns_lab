from threading import Lock # Модуль для работы с многозадачностью

# Мета-класс для реализации паттерна Одиночка
class SingletonMeta(type):
    _instances = {}  # Словарь для хранения экземпляров классов, использующих этот мета-класс
    _lock = Lock()  # Объект блокировки для обеспечения потока-безопасности

    # Метод, который вызывается при создании нового экземпляра класса
    def __call__(cls, *args, **kwargs):
        with cls._lock:  # Блокируем доступ, чтобы создать экземпляр только для одного потока
            if cls not in cls._instances:  # Если экземпляр еще не создан
                instance = super().__call__(*args, **kwargs)  # Создаем новый экземпляр
                cls._instances[cls] = instance  # Сохраняем экземпляр в словарь
        return cls._instances[cls]  # Возвращаем уже созданный экземпляр или тот, что только что был создан

# Класс Logger, использующий мета-класс SingletonMeta
class Logger(metaclass=SingletonMeta):
    @staticmethod
    def log(message):
        print(f'Log: {message}')  # Метод для вывода сообщения в лог

if __name__ == '__main__':
    # Создаем два объекта Logger
    logger1 = Logger()
    logger2 = Logger()

    # Логирование
    logger1.log('Сообщение.')
    logger2.log('Следующее сообщение.')

    # Проверка: это один и тот же экземпляр!
    print(id(logger1) == id(logger2))

    # Просто для наглядности
    print(SingletonMeta._instances) # <class '__main__.Logger'>: <__main__.Logger object at 0x00000248C04DA270>

