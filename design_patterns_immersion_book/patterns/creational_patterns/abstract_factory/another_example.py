from abc import ABC, abstractmethod


# Абстрактные продукты
class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class TextField(ABC):
    @abstractmethod
    def render(self):
        pass


class Menu(ABC):
    @abstractmethod
    def render(self):
        pass


# Конкретные продукты для Windows
class WindowsButton(Button):
    def render(self):
        return 'Windows Button'


class WindowsTextField(TextField):
    def render(self):
        return 'Windows Text Field'


class WindowsMenu(Menu):
    def render(self):
        return 'Windows Menu'


# Конкретные продукты для MacOS
class MacOSButton(Button):
    def render(self):
        return 'MacOS Button'


class MacOSTextField(TextField):
    def render(self):
        return 'MacOS Text Field'


class MacOSMenu(Menu):
    def render(self):
        return 'MacOS Menu'


# Абстрактная фабрика
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_text_field(self) -> TextField:
        pass

    @abstractmethod
    def create_menu(self) -> Menu:
        pass


# Конкретные фабрики для Windows и MacOS
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_text_field(self) -> TextField:
        return WindowsTextField()

    def create_menu(self) -> Menu:
        return WindowsMenu()


class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_text_field(self) -> TextField:
        return MacOSTextField()

    def create_menu(self) -> Menu:
        return MacOSMenu()


if __name__ == '__main__':
    # Клиентский код
    def client_code(components: list):
        for component in components:
            instance = component()
            print(instance.render())


    print()
    # Используем только кнопку и текстовое поле для Windows
    windows_factory = WindowsFactory()
    client_code([
        windows_factory.create_button,
        windows_factory.create_text_field
    ])

    print()
    # Используем только меню для MacOS
    macos_factory = MacOSFactory()
    client_code([macos_factory.create_menu])
