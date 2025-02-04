from abc import ABC, abstractmethod

"""
Вариант:
    2) Поиск подходящего обработчика
"""


class Handler(ABC):
    """Интерфейс обработчика."""

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class BaseHandler(Handler):
    """Базовый обработчик с передачей запроса дальше."""

    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class HandlerA(BaseHandler):
    """Конкретный обработчик A."""

    def handle(self, request):
        if request == 'A':
            return f'HandlerA обработал запрос {request}'
        return super().handle(request)


class HandlerB(BaseHandler):
    """Конкретный обработчик B."""

    def handle(self, request):
        if request == 'B':
            return f'HandlerB обработал запрос {request}'
        return super().handle(request)


class HandlerC(BaseHandler):
    """Конкретный обработчик C."""

    def handle(self, request):
        if request == 'C':
            return f'HandlerC обработал запрос {request}'
        return super().handle(request)


if __name__ == '__main__':
    h1 = HandlerA()
    h2 = HandlerB()
    h3 = HandlerC()

    h1.set_next(h2).set_next(h3)

    for req in ['B', 'A', 'C', 'D']:
        result = h1.handle(req)
        print(result if result else f'Нет обработчика для запроса {req}')
