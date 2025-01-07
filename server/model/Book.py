from sqlalchemy.orm import DeclarativeBase
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .Base import Base

from modeldto.Book import Book as BookDto

class Book(Base):

    __tablename__ = 'book_book'


    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String())
    author: Mapped[str]= mapped_column(String())
    tags: Mapped[str]= mapped_column(Text())
    numeric: Mapped[bool] = mapped_column(Boolean())
    price: Mapped[int] = mapped_column(Integer())
    quantity: Mapped[int] = mapped_column(Integer())

    bookshop: Mapped['BookShop'] = relationship(back_populates='books')
    bookshop_id: Mapped[int] = mapped_column(ForeignKey('book_bookshop.id'))
    bookcase_id: Mapped[int] = mapped_column(ForeignKey('book_bookcase.id'))

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.tags}, {self.numeric}, {self.price}, {self.quantity})"

    @classmethod
    def from_dto(cls, bookdto):
        return Book(
            title = bookdto.title,
            author = bookdto.author,
            tags = bookdto.tags,
            numeric = bookdto.numeric,
            price = bookdto.price,
            quantity = bookdto.quantity,
        )

    def to_dto(self):
        return BookDto(
            title = self.title,
            author = self.author,
            tags = self.tags,
            numeric = self.numeric,
            price = self.price,
            quantity = self.quantity
        )
