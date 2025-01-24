# Нарушение DIP: верхний уровень зависит от конкретной реализации

class Keyboard1:
    @staticmethod
    def input():
        return 'Ввод с клавиатуры.'


class Monitor1:
    @staticmethod
    def display(message):
        print(message)


class Computer1:
    def __init__(self):
        self.keyboard = Keyboard()  # Прямая зависимость от конкретного класса
        self.monitor = Monitor()  # Прямая зависимость от конкретного класса

    def operate(self):
        input_data = self.keyboard.input()
        self.monitor.display(input_data)


# if __name__ == '__main__':
# computer = Computer()
# computer.operate()

# Исправление DIP:
#  внедряем абстракции через интерфейсы или базовые классы, чтобы Computer зависел от них, а не от конкретных реализаций

class InputDevice:
    def input(self):
        raise NotImplementedError('Подклассы должны реализовывать этот метод')


class OutputDevice:
    def display(self, message):
        raise NotImplementedError('Подклассы должны реализовывать этот метод')


"""
Классы нижнего уровня реализуют базовые операции вроде
работы с диском, передачи данных по сети, подключения к
базе данных и прочее.
"""


class Keyboard(InputDevice):
    def input(self):
        return 'Ввод с клавиатуры.'


class Monitor(OutputDevice):
    def display(self, message):
        print(message)


"""
Классы высокого уровня содержат сложную бизнес-логику
программы, которая опирается на классы низкого уровня
для осуществления более простых операций.
"""


class Computer:
    def __init__(self, input_device: InputDevice, output_device: OutputDevice):
        self.input_device = input_device
        self.output_device = output_device

    def operate(self):
        input_data = self.input_device.input()
        self.output_device.display(input_data)


if __name__ == '__main__':
    keyboard = Keyboard()
    monitor = Monitor()
    computer = Computer(keyboard, monitor)
    computer.operate()  # Ввод с клавиатуры.
