from abc import ABC, abstractmethod


# # Абстрактный продукт
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


# Класс Грузовик
class Truck(Transport):
    def deliver(self):
        print('\tГруз доставлен по дороге с помощью грузовика.')


# Класс Корабль
class Ship(Transport):
    def deliver(self):
        print('\tГруз доставлен по морю с помощью корабля.')


# Абстрактный класс "Фабрика"
class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self):
        # Используем фабричный метод для создания транспорта
        transport = self.create_transport()
        print('\tПланируем доставку...')
        transport.deliver()


# Конкретная фабрика для грузовиков
class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()


# Конкретная фабрика для кораблей
class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()


# Клиентский код
def client_code(factory: Logistics):
    print(f'\tНачало логистического процесса.')
    factory.plan_delivery()
    print('\tЛогистический процесс завершён.')


if __name__ == '__main__':
    # Выбираем, какую фабрику использовать
    print('Используем дорожную логистику:')
    road_factory = RoadLogistics()
    client_code(road_factory)

    print('\nИспользуем морскую логистику:')
    sea_factory = SeaLogistics()
    client_code(sea_factory)
