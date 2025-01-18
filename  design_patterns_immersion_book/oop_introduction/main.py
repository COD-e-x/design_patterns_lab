
# 1. Зависимость
"""
Определение: Класс A зависит от класса B, если изменения в классе B могут повлиять на работу класса A.
Пример: Класс A использует методы или свойства класса B временно, например, в рамках выполнения одной операции.
"""
# класс B
class Printer:
    @classmethod
    def print_message(cls, message):
        print(message)

# класс A
class Report:
    @classmethod
    def generate(cls):
        printer = Printer()
        printer.print_message('Отчет создан.')

report = Report()
report.generate() # Вывод: Отчет создан.

# 2. Ассоциация и ниже Агрегация - разница не в коде, а в семантике, то есть в том, что подразумевает разработчик:
"""
Определение: Объект A знает об объекте B. Класс A имеет ссылки на объекты класса B и может взаимодействовать с ними.
Пример: Класс A имеет объект B как свойство.

В ассоциации объекты связаны, но независимы.
"""

# класс B
class Driver:
    def __init__(self, name):
        self.name = name

# класс A
class Car:
    def __init__(self, model, driver: Driver):
        self.model = model
        self.driver = driver

    def drive(self):
        print(f'{self.driver.name} ведет {self.model}.')

driver_ = Driver('Иван')
car = Car('Tesla', driver_)
car.drive() # Вывод: Иван ведет Tesla.

# 3. Агрегация
"""
Определение: Объект A состоит из объекта B, но объект B может существовать независимо от объекта A.
Пример: Класс A содержит ссылку на объект B, но B не уничтожается, если A удалён.

В агрегации объекты составляют "целое", но части могут существовать отдельно.
"""

# класс B
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

# класс A
class OtherCar:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

engine_ = Engine(250)
other_car = OtherCar('BMW', engine_)
print(f'Мощность двигателя: {other_car.engine.horsepower}.') # Вывод: Мощность двигателя: 1000.


# 4. Композиция
"""
Определение: Объект A управляет жизненным циклом объекта B. Если A уничтожается, то B тоже уничтожается.
Пример: Объект B создаётся внутри объекта A, и его существование полностью зависит от A.
"""

# используем class Engine реализованный выше, так как его существование отдельно от класса А возможна!

class Truck:
    def __init__(self, model, horsepower):
        self.model = model
        self.engine = Engine(horsepower)


truck = Truck('Volvo', 650)
print(f'Мощность двигателя: {truck.engine.horsepower}.') # Вывод: Мощность двигателя: 1000.


# 5. Реализация
"""
Определение: Класс A реализует методы, объявленные в интерфейсе B. 
Объекты класса A могут рассматриваться через интерфейс B.
"""

from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class OtherReport(Printable):
    def print(self):
        print('Отчет напечатан.')

other_report = OtherReport()
other_report.print() # Вывод: Отчет напечатан!


"""
Определение: Класс A наследует свойства и методы класса B. 
Он может переопределять их или добавлять новые. Объекты A можно использовать в контексте класса B.
"""

class Animal:
    def speak(self):
        print('Животное издаёт звук.')

class Dog(Animal):
    def speak(self):
        print('Собака лает.')

animal = Animal()
animal.speak()

dog = Dog()
dog.speak() # Вывод: Собака лает.