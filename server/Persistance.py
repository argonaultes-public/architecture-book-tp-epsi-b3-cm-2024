from abc import ABC, abstractmethod
import os
import jsonpickle

from model import Book, BookShop

class Persistance(ABC):

    @abstractmethod
    def save(self, bookshop, user):
        pass

    @abstractmethod
    def reload(self):
        pass

class PersistanceDB(Persistance):

    def save(self, bookshop, user):
        print('save in db')

    def reload(self):
        print('reload from db')
        return None, None

class PersistanceFile(Persistance):

    __json_file = "application-bib.json"

    def save(self, bookshop, user):
        with open(self.__json_file, "w") as f:
            f.write(jsonpickle.encode({"bookshop": bookshop, "user": user}))

    def reload(self):
        if not os.path.exists(self.__json_file):
            print(f'Fichier {self.__json_file} introuvable.')
            return BookShop.BookShop(), None
        with open(self.__json_file, "r") as f:
            application = jsonpickle.decode(f.read())
            return application['bookshop'], application['user']
