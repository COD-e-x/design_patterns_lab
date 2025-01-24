# Нарушение LSP: дочерний класс меняет поведение базового класса
from abc import ABC, abstractmethod


class Bird1(ABC):
    @abstractmethod
    def fly(self):
        return 'Я лечу!'


class Sparrow1(Bird1):
    def fly(self):
        return 'Я лечу!'


"""
```Метод не должен выбрасывать исключения, которые не
свойственны базовому методу```
Метод `fly` в подклассе `Penguin1` нарушает ожидания, заложенные в базовом классе `Bird1`, 
выбрасывая исключение вместо предоставления реализации.
"""


class Penguin1(Bird1):
    def fly(self):
        raise NotImplementedError('Нет, спасибо! Знаете, а может сами полетите?!')


# Исправление LSP: используем более общий базовый класс и интерфейсы, чтобы различать поведение

class Bird(ABC):
    @abstractmethod
    def move(self):
        raise NotImplementedError('Подклассы должны реализовывать этот метод.')


"""
Типы параметров метода подкласса должны совпадать или
быть более абстрактными, чем типы параметров базового
метода. 
"""


class FlyingBird(Bird):
    def move(self):
        return 'Я лечу!'


class NonFlyingBird(Bird):
    def move(self):
        return 'Я иду пешком!'


class Sparrow(FlyingBird):
    pass


"""
Тип возвращаемого значения метода подкласса должен 
совпадать или быть подтипом возвращаемого значения базового метода.
"""


class Penguin(NonFlyingBird):
    pass


if __name__ == '__main__':
    # Работает с любым объектом, унаследованным от `Bird`, без изменения своего кода
    def make_bird_move(bird):
        print(bird.move())


    sparrow = Sparrow()
    make_bird_move(sparrow)

    penguin = Penguin()
    make_bird_move(penguin)
