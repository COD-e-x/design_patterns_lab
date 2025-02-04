from abc import ABC, abstractmethod


class Strategy(ABC):
    """Абстрактный класс стратегии для выполнения операции."""

    @abstractmethod
    def execute(self, a, b):
        """Метод для выполнения операции."""
        pass


class ConcreteStrategyAdd(Strategy):
    """Стратегия для сложения двух чисел."""

    def execute(self, a, b):
        return a + b


class ConcreteStrategySubtract(Strategy):
    """Стратегия для вычитания двух чисел."""

    def execute(self, a, b):
        return a - b


class ConcreteStrategyMultiply(Strategy):
    """Стратегия для умножения двух чисел."""

    def execute(self, a, b):
        return a * b


class Context:
    """Контекст, который работает с выбранной стратегией."""

    def __init__(self, strategy: Strategy):
        """Инициализация с конкретной стратегией."""
        self.strategy = strategy

    def set_strategy(self, strategy: Strategy):
        """Изменение стратегии."""
        self.strategy = strategy

    def execute_strategy(self, a, b):
        """Выполнение операции с текущей стратегией."""
        return self.strategy.execute(a, b)


def main():
    """Демонстрация паттерна стратегии."""
    context = Context(ConcreteStrategyAdd())

    while True:
        try:
            n1 = int(input('Введите первое число: '))
            n2 = int(input('Введите второе число: '))
        except ValueError:
            print('Введите корректное число.')
            continue

        action = input('Выберите операцию: \n\t+ для сложения\n\t- для вычитания\n\t* для умножения\n')

        if action == '+':
            context.set_strategy(ConcreteStrategyAdd())
        elif action == '-':
            context.set_strategy(ConcreteStrategySubtract())
        elif action == '*':
            context.set_strategy(ConcreteStrategyMultiply())
        else:
            print('Некорректная операция!')
            continue

        result = context.execute_strategy(n1, n2)
        print(f'Результат: {result}')
        return


if __name__ == '__main__':
    main()
