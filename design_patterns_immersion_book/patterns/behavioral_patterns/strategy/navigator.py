from abc import ABC, abstractmethod


class RouteStrategy(ABC):
    """Абстрактный класс для стратегии маршрута."""

    @abstractmethod
    def build_route(self, a, b):
        """Метод для построения маршрута от a до b."""
        pass


class RoadStrategy(RouteStrategy):
    """Стратегия маршрута по дороге."""

    def build_route(self, a, b):
        return f'Построение маршрута по дороге от {a} до {b}'


class PublicTransportStrategy(RouteStrategy):
    """Стратегия маршрута на общественном транспорте."""

    def build_route(self, a, b):
        return f'Построение маршрута на общественном транспорте от {a} до {b}'


class WalkingStrategy(RouteStrategy):
    """Стратегия пешеходного маршрута."""

    def build_route(self, a, b):
        return f'Построение пешеходного маршрута от {a} до {b}'


class Navigator:
    """Навигатор, использующий стратегию маршрута."""

    def __init__(self, route_strategy: RouteStrategy):
        """Инициализация с конкретной стратегией маршрута."""
        self.route_strategy = route_strategy

    def set_route_strategy(self, route_strategy: RouteStrategy):
        """Изменение стратегии маршрута."""
        self.route_strategy = route_strategy

    def build_route(self, a, b):
        """Построение маршрута с использованием текущей стратегии."""
        return self.route_strategy.build_route(a, b)


if __name__ == '__main__':
    road_strategy = RoadStrategy()
    public_transport_strategy = PublicTransportStrategy()
    walking_strategy = WalkingStrategy()

    navigator = Navigator(road_strategy)
    print(navigator.build_route('Москва', 'Сочи'))

    navigator.set_route_strategy(public_transport_strategy)
    print(navigator.build_route('Сочи', 'Краснодар'))

    navigator.set_route_strategy(walking_strategy)
    print(navigator.build_route('Краснодар, улица А', 'Краснодар, улица Б'))
