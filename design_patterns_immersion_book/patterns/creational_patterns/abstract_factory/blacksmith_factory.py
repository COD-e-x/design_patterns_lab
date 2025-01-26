from abc import ABC, abstractmethod


# Абстрактный продукты
class Sword(ABC):
    @abstractmethod
    def create(self):
        pass


class Armor(ABC):
    @abstractmethod
    def create(self):
        pass


class Spear(ABC):
    @abstractmethod
    def create(self):
        pass


# Конкретные продукты для Норвежского кузнеца
class VikingSword(Sword):
    def create(self):
        print('\tСоздал меч викингов.')


class VikingArmor(Armor):
    def create(self):
        print('\tСоздал броню викингов.')


class VikingSpear(Spear):
    def create(self):
        print('\tСоздал копье викингов.')


# Конкретные продукты для Японского кузнеца
class SamuraiSword(Sword):
    def create(self):
        print('\tСоздал меч самураев.')


class SamuraiArmor(Armor):
    def create(self):
        print('\tСоздал броню самураев.')


class SamuraiSpear(Spear):
    def create(self):
        print('\tСоздал копье самураев.')


# Абстрактная фабрика
class Blacksmith(ABC):
    @abstractmethod
    def create_sword(self):
        pass

    @abstractmethod
    def create_armor(self):
        pass

    @abstractmethod
    def create_spear(self):
        pass


# Конкретные фабрики для кузнецов
class NorwegianBlacksmithFactory(Blacksmith):
    def create_sword(self):
        return VikingSword()

    def create_armor(self):
        return VikingArmor()

    def create_spear(self):
        return VikingSpear()


class JapaneseBlacksmithFactory(Blacksmith):
    def create_sword(self):
        return SamuraiSword()

    def create_armor(self):
        return SamuraiArmor()

    def create_spear(self):
        return SamuraiSpear()


if __name__ == '__main__':
    # Клиентский код
    def client_code(blacksmith: Blacksmith):
        sword = blacksmith.create_sword()
        armor = blacksmith.create_armor()
        spear = blacksmith.create_spear()

        sword.create()
        armor.create()
        spear.create()


    norwegian_blacksmith = NorwegianBlacksmithFactory()
    japanese_blacksmith = JapaneseBlacksmithFactory()

    print('Кузнец викингов:')
    client_code(norwegian_blacksmith)

    print('\nКузнец самураев:')
    client_code(japanese_blacksmith)
