model/
    
    book.py
    
    from abc import ABC, abstractmethod
    
    class BookFactory(ABC):
        @abstractmethod
        def create_book(self, title, author, year):
            pass
    
    class RegularBookFactory(BookFactory):
        def create_book(self, title, author, year):
            return Book(title, author, year)
    
    class Book:
        def __init__(self, title, author, year):
            self.title = title
            self.author = author
            self.year = year
    
    
    
        def __repr__(self):
            return f"Book(title={self.title}, author={self.author}, year={self.year})"
    
        def __str__(self):
            return f'Книга {self.title}, автор {self.author}, год {self.year}'
    
    reader.py
    
    from abc import ABC, abstractmethod
    
    
    class ReaderFactory(ABC):
        @abstractmethod
        def create_reader(self, name, reader_id):
            pass
    
    
    class RegularReaderFactory(ReaderFactory):
        def create_reader(self, name, reader_id):
            return Reader(name, reader_id)
    
    
    class Reader:
        def __init__(self, name, reader_id):
            self.name = name
            self.reader_id = reader_id
            self.borrowed_books = []
    
        def borrow_book(self, book):
            """Метод для взятия книги"""
            if book not in self.borrowed_books:
                self.borrowed_books.append(book)
            else:
                raise ValueError(f"{self.name} эта книга у тебя дома на полке '{book.title}'.")
    
        def return_book(self, book):
            """Метод для возврата книги"""
            if book in self.borrowed_books:
                self.borrowed_books.remove(book)
            else:
                raise ValueError(f"{self.name} ты не брал книгу '{book.title}', у тебя его нет.")
    
        def __repr__(self):
            return f"Reader(name={self.name}, reader_id={self.reader_id})"
    
        def __str__(self):
            return f"Читатель {self.name}, идентификатор читателя {self.reader_id})"
    
    liabrian.py
    
    from abc import ABC, abstractmethod
    
    class LibrarianFactory(ABC):
        @abstractmethod
        def create_librarian(self, name, employee_id):
            pass
    
    class RegularLibrarianFactory(LibrarianFactory):
        def create_librarian(self, name, employee_id):
            return Librarian(name, employee_id)
    
    class Librarian:
        def __init__(self, name, employee_id):
            self.name = name
            self.employee_id = employee_id
    
        def assign_book(self, book, reader):
            reader.borrow_book(book)
    
        def remove_book(self, book, library):
            library.remove_book(book)
    
        def __repr__(self):
            return f"Librarian(name={self.name}, employee_id={self.employee_id})"
    
        def __str__(self):
            return f'Библиотекарь {self.name}, идентификатор сотрудника {self.employee_id}'

service/

    