from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def move(self):
        pass


class CombustionEngine(Engine):
    def move(self):
        return 'Двигатель внутреннего сгорания запускается.'


class ElectricEngine(Engine):
    def move(self):
        return 'Электрический двигатель запускается.'


class Driver(ABC):
    @abstractmethod
    def navigate(self):
        pass


class Robot(Driver):
    def navigate(self):
        return 'Навигация с помощью Робота.'


class Human(Driver):
    def navigate(self):
        return 'Навигация с помощью человека.'


class Transport:
    def __init__(self, engine_type: str, driver: Driver):
        self.__engine = self.create_engine(engine_type)
        self.__driver = driver

    @staticmethod
    def create_engine(engine_type: str) -> Engine:
        if engine_type == 'combustion':
            return CombustionEngine()
        elif engine_type == 'electric':
            return ElectricEngine()
        else:
            raise ValueError('Неизвестный тип двигателя')

    def deliver(self, destination, cargo):
        engine_status = self.__engine.move()
        driver_status = self.__driver.navigate()
        return f'Доставка: {cargo} в {destination}. {engine_status} {driver_status}'


if __name__ == '__main__':
    engine_1 = 'combustion'
    driver_1 = Human()

    transport = Transport(engine_1, driver_1)

    result = transport.deliver('Москва', 'Шоколад')
    print(f'\n{result}')
