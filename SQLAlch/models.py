import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=255), unique=True)


class Book(Base):
    __tablename__ = 'book'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String(length=255))
    publisher_id = sqlalchemy.Column(sqlalchemy.ForeignKey('publisher.id'), nullable=False)
    publisher = relationship(Publisher, backref='book')

    def __str__(self):
        return f'{self.title}'


class Shop(Base):
    __tablename__ = 'shop'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=255))

    def __str__(self):
        return f'{self.name}'

class Stock(Base):
    __tablename__ = 'stock'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    book_id = sqlalchemy.Column(sqlalchemy.ForeignKey('book.id'), nullable=False)
    book = relationship(Book, backref='book_stock')
    shop_id = sqlalchemy.Column(sqlalchemy.ForeignKey('shop.id'), nullable=False)
    shop = relationship(Shop, backref='shop_stock')
    count = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

class Sale(Base):
    __tablename__ = 'sale'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    price = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    date_sale = sqlalchemy.Column(sqlalchemy.Date)
    stock_id = sqlalchemy.Column(sqlalchemy.ForeignKey('stock.id'), nullable=False)
    stock = relationship(Stock, backref='sale')
    count = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    def __str__(self):
        return str(self.price)


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)








