from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_click(self):
        pass


class WindowsButton(Button):
    def render(self):
        print('Отрисовать кнопку в стиле Windows.')

    def on_click(self):
        print('Навесить на кнопку обработчик событий Windows.')


class HTMLButton(Button):
    def render(self):
        print('Вернуть HTML-код кнопки.')

    def on_click(self):
        print('Навесить на кнопку обработчик событий браузера.')


class Dialog(ABC):
    @abstractmethod
    def create_button(self):
        pass

    def render(self, ):
        ok_button = self.create_button()
        ok_button.on_click()
        ok_button.render()


class WindowsDialog(Dialog):
    def create_button(self):
        return WindowsButton()


class WebDialog(Dialog):
    def create_button(self):
        return HTMLButton()


class Application:
    def __init__(self):
        self.dialog = None

    def initialize(self):
        config = self.read_application_config_file()
        if config['OS'] == 'Windows':
            self.dialog = WindowsDialog()
        elif config['OS'] == 'Web':
            self.dialog = WebDialog()
        else:
            raise Exception('Ошибка! Неизвестная операционная система.')

    @staticmethod
    def read_application_config_file():
        return {'OS': 'Web'}

    def main(self):
        self.initialize()
        self.dialog.render()


if __name__ == '__main__':
    a = Application()
    a.main()
