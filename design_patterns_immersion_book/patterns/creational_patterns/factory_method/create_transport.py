from abc import ABC, abstractmethod


class Transport(ABC):
    """Абстрактный класс продукт."""

    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):
    """Класс грузовик (конкретный продукт для создания фабрикой)."""

    def deliver(self):
        print('\tГруз доставлен по дороге с помощью грузовика.')


class Ship(Transport):
    """Класс Корабль (конкретный продукт для создания фабрикой)."""

    def deliver(self):
        print('\tГруз доставлен по морю с помощью корабля.')


class Logistics(ABC):
    """Абстрактный класс фабрика, для реализации паттерна фабричный метод."""

    @abstractmethod
    def create_transport(self):
        pass


class RoadLogistics(Logistics):
    """Фабрика для конкретного продукта, определенного в нем. В данном случае грузовика."""

    def create_transport(self):
        return Truck()


class SeaLogistics(Logistics):
    """Фабрика для конкретного продукта, определенного в нем. В данном случае корабля."""

    def create_transport(self):
        return Ship()


class DeliveryService:
    """Класс для реализации логистики."""

    @staticmethod
    def plan_delivery(logistics: Logistics):
        transport = logistics.create_transport()
        print('\tПланируем доставку...')
        transport.deliver()


def client_code(logistics: Logistics):
    """Клиентский код."""
    print(f'\tНачало логистического процесса.')
    delivery_service.plan_delivery(logistics)
    print('\tЛогистический процесс завершён.')


if __name__ == '__main__':
    road_factory = RoadLogistics()
    sea_factory = SeaLogistics()
    delivery_service = DeliveryService()

    # Выбираем, какую фабрику использовать

    print('\nИспользуем дорожную логистику:')
    client_code(road_factory)

    print('\nИспользуем морскую логистику:')
    client_code(sea_factory)
