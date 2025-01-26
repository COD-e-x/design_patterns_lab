from abc import ABC, abstractmethod


class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass

    def set_model(self, model):
        pass

    @abstractmethod
    def set_seats(self, number):
        pass

    @abstractmethod
    def set_engine(self, engine):
        pass

    @abstractmethod
    def set_trip_computer(self, trip_computer=False):
        pass

    @abstractmethod
    def set_gps(self, gps=False):
        pass

    @abstractmethod
    def get_result(self):
        pass


class Car:
    def __init__(self):
        self.model_car = None
        self.seats = None
        self.engine = None
        self.trip_computer = False
        self.gps = False

    def __str__(self):
        return f'Автомобиль {self.model_car}'


class Manual:
    def __init__(self):
        self.model_car = None
        self.seats = None
        self.engine = None
        self.trip_computer = False
        self.gps = False

    def __str__(self):
        trip_computer_str = (
            '\n\tруководство системы навигации' if self.trip_computer else ""
        )
        gps_str = (
            '\n\tинструкция по GPS' if self.trip_computer else ""
        )
        return f"""Руководство для автомобиля {self.model_car}:
    количество мест {self.seats}
    описание двигателя {self.engine}{trip_computer_str}{gps_str}"""


class CarBuilder(Builder):
    def __init__(self):
        self.__car = None

    def reset(self):
        self.__car = Car()

    def set_model(self, model):
        self.__car.model_car = model

    def set_seats(self, number):
        self.__car.seats = number

    def set_engine(self, engine):
        self.__car.engine = engine

    def set_trip_computer(self, trip_computer=False):
        self.__car.trip_computer = trip_computer

    def set_gps(self, gps=False):
        self.__car.gps = gps

    def get_result(self):
        return self.__car


class CarManualBuilder(Builder):
    def __init__(self):
        self.__manual = None

    def reset(self):
        self.__manual = Manual()

    def set_model(self, model):
        self.__manual.model_car = model

    def set_seats(self, number):
        self.__manual.seats = number

    def set_engine(self, engine):
        self.__manual.engine = engine

    def set_trip_computer(self, trip_computer=False):
        self.__manual.trip_computer = trip_computer

    def set_gps(self, gps=False):
        self.__manual.gps = gps

    def get_result(self):
        return self.__manual


class Director:
    def __init__(self, builder: Builder):
        self.builder = builder

    def make_suv(self):
        self.builder.reset()
        self.builder.set_model('Volvo')
        self.builder.set_seats(5)
        self.builder.set_engine('V6')
        self.builder.set_trip_computer(True)
        self.builder.set_gps(True)
        self.builder.get_result()

    def make_sports_car(self):
        self.builder.reset()
        self.builder.set_model('BMW')
        self.builder.set_seats(2)
        self.builder.set_engine('V8')
        self.builder.set_trip_computer()
        self.builder.set_gps()
        self.builder.get_result()


if __name__ == '__main__':
    def car1():
        # Создаем и выводим автомобиль
        car_builder = CarBuilder()
        director = Director(car_builder)
        director.make_suv()
        print(car_builder.get_result())

        # Создаем и выводим руководство
        manual_builder = CarManualBuilder()
        director_manual = Director(manual_builder)
        director_manual.make_suv()
        print(manual_builder.get_result())


    car1()
    print()


    def car2():
        # Создаем и выводим автомобиль
        car_builder = CarBuilder()
        director = Director(car_builder)
        director.make_sports_car()
        print(car_builder.get_result())

        # Создаем и выводим руководство
        manual_builder = CarManualBuilder()
        director_manual = Director(manual_builder)
        director_manual.make_sports_car()
        print(manual_builder.get_result())


    car2()
