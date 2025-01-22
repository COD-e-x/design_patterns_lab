from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def get_nutrition(self):
        pass


class Sausage(Food):
    def __init__(self, color, expiration_date):
        self.color = color
        self.expiration_date = expiration_date

    def get_nutrition(self):
        return 50

    def get_color(self):
        return self.color

    def get_expiration(self):
        return self.expiration_date


class Cat:
    def __init__(self, energy=100):
        self.energy = energy

    def eat(self, food: Food):
        nutrition = food.get_nutrition()
        self.energy += nutrition
        print(f'Кот съел и набрал {nutrition} энергии. Текущая энергия: {self.energy}')


if __name__ == '__main__':
    cat = Cat()
    sausage = Sausage(color='red', expiration_date='2025-12-31')
    cat.eat(sausage)

    # Дополнительно можно получить информацию о колбасе
    print(f'Цвет сосиски: {sausage.get_color()}')
    print(f'Срок годности сосисок: {sausage.get_expiration()}')
