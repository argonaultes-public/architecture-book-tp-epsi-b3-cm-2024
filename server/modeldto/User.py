from .BookCase import BookCase

class User:
    def __init__(self, username):
        self.__username = username
        self.__bookcase =  BookCase(username + "_bookcase", [])

    @property
    def username(self):
        return self.__username
    