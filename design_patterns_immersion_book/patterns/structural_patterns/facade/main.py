from abc import ABC, abstractmethod


class BookFactory(ABC):
    """Абстрактная фабрика книг."""

    @abstractmethod
    def create_book(self, title):
        pass


class ReaderFactory(ABC):
    """Абстрактная фабрика читателей."""

    @abstractmethod
    def create_reader(self, name, reader_id):
        pass


class PrintedBookFactory(BookFactory):
    """Фабрика печатных книг."""

    def create_book(self, title):
        return PrintedBook(title)


class PrintedBook:
    """
    Инициализация книги.

    :param title: Название книги.
    """

    def __init__(self, title):
        self.title = title
        self.available = True


class CoreReaderFactory(ReaderFactory):
    """Фабрика для основных читателей."""

    def create_reader(self, name, reader_id):
        return CoreReader(name, reader_id)


class CoreReader:
    """
    Инициализация читателя.

    :param name: Имя читателя.
    :param reader_id: Уникальный идентификатор читателя.
    """

    def __init__(self, name, reader_id):
        self.name = name
        self.reader_id = reader_id
        self.borrowed_books = []


class Library:
    """Инициализация библиотеки."""

    def __init__(self, book_factory: BookFactory, reader_factory: ReaderFactory):
        self.books = {}
        self.readers = {}
        self.book_factory = book_factory
        self.reader_factory = reader_factory

    def get_books(self):
        """Получить статус всех книг в библиотеке в виде списка."""
        result = {}
        for book in self.books.values():
            temp = 'Книга в библиотеке' if book.available else 'Книга у читателя'
            result[book.title] = {
                'available': temp,
            }
        return result

    def get_readers(self):
        """Получить список всех читателей и информацию о книгах, которые они взяли."""
        result = {}
        for reader in self.readers.values():
            result[reader.name] = {
                'reader_id': reader.reader_id,
                'borrowed_books': [book.title for book in reader.borrowed_books]
            }
        return result

    def add_book(self, title):
        """
        Добавить книгу в библиотеку.

        :param title: Название книги.
        """
        book = self.book_factory.create_book(title)
        self.books[book.title] = book

    def add_reader(self, name, reader_id):
        """
        Добавить читателя в библиотеку.

        :param name: Имя читателя.
        :param reader_id: Уникальный идентификатор читателя.
        """
        reader = self.reader_factory.create_reader(name, reader_id)
        self.readers[reader.name] = reader

    def borrow_book(self, reader_name, book_title):
        """
        Оформить выдачу книги.

        :param reader_name: Имя читателя.
        :param book_title: Название книги.
        """
        book = self.books.get(book_title)
        reader = self.readers.get(reader_name)
        if reader_name not in self.readers:
            return f'Читателя {reader_name} нет в базе данных библиотеки.'
        elif book_title not in self.books:
            return f'Книга {book_title} не найдена в библиотеке.'
        else:
            if book.available:
                book.available = False
                reader.borrowed_books.append(book)
                return f'Книга "{book.title}" успешно выдана читателю {reader.name}.'
            else:
                return f'Книга "{book.title}" выдана читателю и сейчас недоступна.'

    def return_book(self, reader_name, book_title):
        """
        Вернуть книгу в библиотеку.

        :param reader_name: Имя читателя.
        :param book_title: Название книги.
        """
        book = self.books.get(book_title)
        reader = self.readers.get(reader_name)
        if reader_name not in self.readers:
            return f'Читателя {reader} нет в базе данных библиотеки.'
        elif book_title not in self.books:
            return f'Книга {book} не найдена в библиотеке.'
        else:
            if not book.available:
                book.available = True
                reader.borrowed_books.remove(book)
                return f'Книга "{book.title}" возвращена в библиотеку.'
            else:
                return f'Книга "{book.title}" выдана читателю и сейчас недоступна.'


class LibraryFacade:
    """
    Инициализация фасада для работы с библиотекой.

    :param library: Объект библиотеки.
    """

    def __init__(self, library: Library):
        self.library = library

    def get_books_status(self):
        """
        Получить статус всех книг в библиотеке через фасад.

        :return: Статус книг в библиотеке.
        """
        return self.library.get_books()

    def get_readers_status(self):
        """
        Получить информацию о читателях через фасад.

        :return: Статус читателей.
        """
        return self.library.get_readers()

    def add_book_to_library(self, title):
        """
        Добавить книгу в библиотеку через фасад.

        :param title: Название книги.
        """
        self.library.add_book(title)

    def add_reader_to_library(self, name, reader_id):
        """
        Добавить читателя в библиотеку через фасад.

        :param name: Имя читателя.
        :param reader_id: Идентификатор читателя.
        """
        self.library.add_reader(name, reader_id)

    def borrow_book(self, reader_name, book_title):
        """
        Оформить выдачу книги через фасад.

        :param reader_name: Имя читателя.
        :param book_title: Название книги.
        :return: Информация о результате в образовательных целях.
        """
        return self.library.borrow_book(reader_name, book_title)

    def return_book(self, reader_name, book_title):
        """
        Вернуть книгу в библиотеку через фасад.

        :param reader_name: Имя читателя.
        :param book_title: Название книги.
        :return: Информация о результате в образовательных целях.
        """
        return self.library.return_book(reader_name, book_title)


if __name__ == '__main__':
    book_factory_ = PrintedBookFactory()
    reader_factory_ = CoreReaderFactory()

    # Создаем библиотеку, передаем фабрики
    library_ = Library(book_factory_, reader_factory_)

    facade = LibraryFacade(library_)

    facade.add_book_to_library('Книга 1')
    facade.add_book_to_library('Книга 2')
    facade.add_book_to_library('Книга 3')
    facade.add_book_to_library('Книга 4')

    facade.add_reader_to_library('Читатель 1', 'id 001')
    facade.add_reader_to_library('Читатель 2', 'id 002')

    print(facade.borrow_book('Читатель 1', 'Книга 1'))
    print(facade.borrow_book('Читатель 1', 'Книга 2'))
    print(facade.borrow_book('Читатель 2', 'Книга 4'))
    print()

    print(facade.get_books_status())
    print(facade.get_readers_status())
    print()

    print(facade.return_book('Читатель 1', 'Книга 1'))
    print(facade.return_book('Читатель 1', 'Книга 2'))
    print(facade.return_book('Читатель 2', 'Книга 4'))
    print()

    print(facade.get_books_status())
    print(facade.get_readers_status())
