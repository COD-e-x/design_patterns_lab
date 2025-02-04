class Editor:
    """Текстовый редактор с управлением."""

    def __init__(self):
        self.text = ""
        self.selection = ""

    def get_selection(self):
        """Возвращает выделенный текст."""
        return self.selection

    def delete_selection(self):
        """Удаляет выделенный текст."""
        self.text = self.text.replace(self.selection, "", 1)
        self.selection = ""

    def replace_selection(self, text):
        """Заменяет выделенный текст."""
        self.text = self.text.replace(self.selection, text, 1)
        self.selection = text


class Command:
    """Базовый класс для команд."""

    def __init__(self, client, editor):
        self.client = client
        self.editor = editor
        self.backup = ""

    def save_backup(self):
        """Сохраняет текущее состояние текста."""
        self.backup = self.editor.text

    def undo(self):
        """Восстанавливает сохраненный текст."""
        self.editor.text = self.backup

    def execute(self):
        """Метод выполнения команды (должен быть переопределен)."""
        pass


class CopyCommand(Command):
    """Команда копирования текста."""

    def execute(self):
        self.client.clipboard = self.editor.get_selection()
        return False


class CutCommand(Command):
    """Команда вырезания текста."""

    def execute(self):
        self.save_backup()
        self.client.clipboard = self.editor.get_selection()
        self.editor.delete_selection()
        return True


class PasteCommand(Command):
    """Команда вставки текста."""

    def execute(self):
        self.save_backup()
        self.editor.replace_selection(self.client.clipboard)
        return True


class UndoCommand(Command):
    """Команда отмены последнего действия."""

    def execute(self):
        self.client.history.pop().undo()
        return False


class CommandHistory:
    """История команд."""

    def __init__(self):
        self.history = []

    def push(self, command):
        """Добавляет команду в историю."""
        self.history.append(command)

    def pop(self):
        """Удаляет и возвращает последнюю команду."""
        return self.history.pop() if self.history else None


class Client:
    """Управляет редактором, буфером обмена и историей команд."""

    def __init__(self):
        self.editors = []
        self.active_editor = Editor()
        self.clipboard = ""
        self.history = CommandHistory()

    def execute_command(self, command):
        """Выполняет команду и добавляет её в историю, если требуется."""
        if command.execute():
            self.history.push(command)

    def undo(self):
        """Отменяет последнюю команду."""
        if self.history.history:
            self.history.pop().undo()


if __name__ == '__main__':
    client = Client()
    editor = client.active_editor
    editor.text = 'Hello, world!'
    editor.selection = 'world'

    # Вырезаем текст
    cut_command = CutCommand(client, editor)
    client.execute_command(cut_command)
    print(editor.text)  # 'Hello, !'
    print(client.clipboard)  # 'world'

    # Отмена последнего действия
    client.undo()
    print(editor.text)  # 'Hello, world!'
