# Нарушение ISP: общий интерфейс с методами, которые не всем нужны
from abc import ABC, abstractmethod


class Worker1(ABC):
    @abstractmethod
    def work(self):
        raise NotImplementedError('Подклассы должны реализовывать этот метод')

    @abstractmethod
    def eat(self):
        raise NotImplementedError('Подклассы должны реализовывать этот метод')


class Programmer1(Worker1):
    def work(self):
        return 'Пишем код.'

    def eat(self):
        return 'Едим пиццу.'


class Robot1(Worker1):
    def work(self):
        return 'Изготавливаем автомобили.'

    def eat(self):  # Ненужный метод для робота
        raise NotImplementedError('Роботы не едят.')


# Исправление ISP: cоздаем узкоспециализированные интерфейсы, чтобы разные классы зависели только от нужных методов

class Workable(ABC):
    @abstractmethod
    def work(self):
        raise NotImplementedError('Подклассы должны реализовывать этот метод')


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        raise NotImplementedError('Подклассы должны реализовывать этот метод')


class Programmer(Workable, Eatable):
    def work(self):
        return 'Пишем код.'

    def eat(self):
        return 'Едим пиццу.'


class Robot(Workable):
    def work(self):
        return 'Изготавливаем автомобили.'


if __name__ == '__main__':
    def perform_work(worker):
        print(worker.work())


    def perform_eat(worker):
        if isinstance(worker, Eatable):
            print(worker.eat())


    programmer = Programmer()
    robot = Robot()

    perform_work(programmer)
    perform_eat(programmer)

    perform_work(robot)
    perform_eat(robot)  # Ничего не выполняет, так как Robot не реализует Eatable
