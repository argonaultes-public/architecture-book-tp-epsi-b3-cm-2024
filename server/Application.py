from model.BookShop import BookShop
from model.Book import Book
from model.Base import Base
from Persistance import Persistance
import os
import jsonpickle
from sqlalchemy import create_engine

class Application:



    def __init__(self, persistance : Persistance):
        self.__persistance = persistance
        self.reload()
        # self.__engine = create_engine('sqlite+pysqlite:///application.db', echo=True)
        # Base.metadata.create_all(self.__engine)

    def add_book_in_bookshop(self, bookdto):
        dto = jsonpickle.decode(bookdto)
        self.__bookshop.books.append(Book.from_dto(bookdto=dto))
        self.save()
        return ('Livre bien ajouté')

    def save(self):
        self.__persistance.save(self.__bookshop, self.__user)


    def reload(self):
        self.__bookshop, self.__user = self.__persistance.reload()


    def display_books(self, *args):
        if self.__bookshop is None:
            return []
        return [book.to_dto() for book in self.__bookshop.books]

    def buy_book(self, book_index):
        book_index = int(book_index)
        try:
            if 0 <= book_index < len(self.__bookshop.books):
                book = self.__bookshop.books[book_index]
                print(book)
                if self.__user.buy_book(self.__bookshop, book):
                    return (f"Vous avez acheté '{book.title}'.")
            else:
                return ("Numéro invalide. Veuillez réessayer.")
        except ValueError:
            return ("Entrée invalide. Veuillez entrer un numéro.")

