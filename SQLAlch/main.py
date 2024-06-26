import datetime
from pprint import pprint
from random import randint

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://postgres:postgres@localhost:5432/alchemy'

engine = create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

pub_list = ['Вита Нова', 'Азбука-Аттикус', 'Норинт']
book_list = [['Чем люди живы', '1'], ['Два брата и золото', '1'], ['Свадьба', '2'], ['Евгений Онегин', '3'],
             ['Руслан и Людмила', '3']]
shop_list = ['Буквоед', 'Лабиринт', 'Книжный дом', 'АЗБука']

stock_list = [['1','1'],['1','2'],['1','3'],['1','4'],
            ['2','1'],['2','2'],['2','3'],['2','4'],
            ['3','1'],['3','2'],['3','3'],['3','4'],
            ['4','1'],['4','2'],['4','3'],['4','4']]

def add_publisher(publisher_list):
    for pib in publisher_list:
        obj = Publisher(name=pib)
        session.add(obj)
        session.commit()


def add_book(book_list):
    for book, author in book_list:
        obj = Book(title=book, publisher_id=author)
        session.add(obj)
        session.commit()


def add_shop(shop_list):
    for shop in shop_list:
        obj = Shop(name=shop)
        session.add(obj)
        session.commit()

def add_stock(stock_list):
    for book, shop in stock_list:
        obj = Stock(book_id=book, shop_id=shop, count=randint(1,999))
        session.add(obj)
        session.commit()

sale_list = [['600','2024-01-01'],['700','2024-09-27'],['800','2024-01-01'],['430','2024-03-06'],
             ['300','2024-08-13'],['900','2024-08-27'],['890','2024-02-02'],['400','2024-03-18'],
             ['350','2024-05-04'],['150','2024-07-27'],['370','2024-03-07'],['700','2024-11-06']]

def add_sale(sale_list):
    for prise, date,in sale_list:
        obj = Sale(price=prise, date_sale=date, stock_id=randint(1,16), count=randint(1,3))
        session.add(obj)
        session.commit()



pub_name_id = input('Введите название издателя или его id')

def get_shop(pub):
    data = session.query(Book).with_entities \
        (Book.title, Shop.name, Sale.price, Sale.date_sale) \
        .join(Publisher, Publisher.id == Book.publisher_id) \
        .join(Stock, Stock.book_id == Book.id) \
        .join(Shop, Shop.id == Stock.shop_id) \
        .join(Sale, Sale.stock_id == Stock.id)
    if pub.isdigit():
        filter_data = data.filter(Publisher.id == pub).all()

    else:
        filter_data = data.filter(Publisher.name == pub).all()
    for title,shop,price,date in filter_data:
        print(f"{title: <40} | {shop: <10} | {price: <8} | {date.strftime('%d-%m-%Y')}")





if __name__ == "__main__":
    # add_publisher(pub_list)
    # add_book(book_list)
    # add_shop(shop_list)
    # add_stock(stock_list)
    # add_sale(sale_list)
    # session.close()
    get_shop(pub_name_id)
