class BookShop:
    def __init__(self, shop_name="", books=None):
        self.__shop_name = shop_name
        if books:
            self.__books = books
        else:
            self.__books = []

    @property
    def books(self):
        return self.__books.copy()

    @property
    def shop_name(self):
        return self.__shop_name

    @shop_name.setter
    def shop_name(self, value):
        self.__shop_name = value

