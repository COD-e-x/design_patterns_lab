from abc import ABC, abstractmethod


# Абстрактный класс сотрудника
class Employee(ABC):
    @abstractmethod
    def do_work(self):
        pass


class Designer(Employee):
    def do_work(self):
        print('Дизайнер начал выполнение своей работы.')


class Artist(Employee):
    def do_work(self):
        print('Артист начал выполнение своей работы.')


class Programmer(Employee):
    def do_work(self):
        print('Программист начал выполнение своей работы.')


class Tester(Employee):
    def do_work(self):
        print('Тестировщик начал выполнение своей работы.')


# Абстрактный класс компании
class Company(ABC):
    @abstractmethod
    def get_employees(self):
        pass

    def create_software(self):
        print('Компания начинает работу...')
        for employee in self.get_employees():
            employee.do_work()
        print('Программное обеспечение готово!')


class GameDev(Company):
    def get_employees(self):
        return [Designer(), Programmer(), Tester()]


class Outsourcing(Company):
    def get_employees(self):
        return [Programmer(), Artist(), Tester()]


if __name__ == '__main__':
    print('Работа компании GameDev:')
    gamedev = GameDev()
    gamedev.create_software()

    print('\nРабота компании Outsourcing:')
    outsourcing = Outsourcing()
    outsourcing.create_software()
