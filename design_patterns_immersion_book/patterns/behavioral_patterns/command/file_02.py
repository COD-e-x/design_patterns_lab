class Task:
    """Задача проекта."""
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        """Завершаем задачу."""
        self.completed = True

    def reopen(self):
        """Возвращаем задачу в незавершенное состояние."""
        self.completed = False


class Command:
    """Базовый класс для команд."""
    def __init__(self, task):
        self.task = task

    def execute(self):
        """Метод выполнения команды (должен быть переопределен)."""
        pass

    def undo(self):
        """Метод для отмены команды (должен быть переопределен)."""
        pass


class CompleteTaskCommand(Command):
    """Команда для завершения задачи."""
    def execute(self):
        self.task.complete()

    def undo(self):
        self.task.reopen()


class ReopenTaskCommand(Command):
    """Команда для возобновления задачи."""
    def execute(self):
        self.task.reopen()

    def undo(self):
        self.task.complete()


class TaskManager:
    """Управляет задачами и их состоянием."""
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        """Выполняет команду и сохраняет её в историю."""
        command.execute()
        self.history.append(command)

    def undo(self):
        """Отменяет последнюю команду."""
        if self.history:
            command = self.history.pop()
            command.undo()

if __name__ == '__main__':
    task_01 = Task('Отложить деньги на отпуск!')
    manager = TaskManager()

    # Завершаем задачу
    complete_command = CompleteTaskCommand(task_01)
    manager.execute_command(complete_command)
    print(task_01.completed)

    # Отменяем завершение задачи
    manager.undo()
    print(task_01.completed)

    """Немного запутано, но смыслы реагирования команд на разные кнопки (можно так выразиться)"""
    # Заново завершаем задачу
    complete_command = CompleteTaskCommand(task_01)
    manager.execute_command(complete_command)
    print(task_01.completed)

    # Возобновляем задачу
    reopen_command = ReopenTaskCommand(task_01)
    manager.execute_command(reopen_command)
    print(task_01.completed)
