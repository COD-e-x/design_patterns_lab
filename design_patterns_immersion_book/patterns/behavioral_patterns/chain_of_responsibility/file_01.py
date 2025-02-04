from __future__ import annotations
from abc import ABC, abstractmethod


class ComponentWithContextualHelp(ABC):
    """Абстрактный класс для компонентов с контекстной помощью."""

    @abstractmethod
    def show_help(self):
        pass


class Component(ComponentWithContextualHelp):
    """Компонент с текстом подсказки и возможностью делегировать помощь контейнеру."""

    def __init__(self, container: Container = None, tooltip_text: str = ''):
        self.__container = container
        self.tooltip_text = tooltip_text

    def show_help(self):
        """Показать подсказку или передать запрос на помощь контейнеру."""
        if self.tooltip_text:
            print(f'Показать подсказку: {self.tooltip_text}')
        elif self.__container:
            print('Нет подсказки, делегируем запрос контейнеру.')
            self.__container.show_help()


class Container(ComponentWithContextualHelp):
    """Контейнер для хранения компонентов и делегирования помощи."""

    def __init__(self, children: list[Component] = None):
        if children is None:
            children = []
        self.__children = children

    def add(self, child: Component):
        """Добавить дочерний компонент в контейнер."""
        self.__children.append(child)

    def show_help(self):
        """Показать помощь для всех дочерних компонентов."""
        for child in self.__children:
            child.show_help()


class Panel(Container):
    """Панель с модальным окном помощи."""

    def __init__(self, modal_help_text: str):
        super().__init__([])
        self.__modal_help_text = modal_help_text

    def show_help(self):
        """Показать модальное окно помощи."""
        print(f'Модальное окно помощи: {self.__modal_help_text}')


class Dialog(Container):
    """Диалог с ссылкой на страницу помощи."""

    def __init__(self, wiki_page_url: str):
        super().__init__([])
        self.wiki_page_url = wiki_page_url

    def show_help(self):
        """Показать ссылку на страницу помощи."""
        print(f'Откройте страницу справки: {self.wiki_page_url}')


if __name__ == '__main__':
    component_1 = Component(tooltip_text='Подсказка для компонента 1')
    component_2 = Component()

    panel = Panel('Модальное окно помощи для панели')
    dialog = Dialog('https://help.example.com')

    container_1 = Container([component_1, component_2, panel, dialog])

    container_1.show_help()
