# coding=utf-8

from .hotel import Hotel
from .craw_html import CrawHTML
from ..base.base import session_factory

session = session_factory()

def populate_database():


    data1 = Hotel()

    data1.name = 'Hotel 1'
    data1.address = 'Dia chi test 1'
    data1.minPrice = 60000
    data1.maxPrice = 550000

    session.add(data1)

    session.commit()
    session.close()


def query_hotels():
    hotels_query = session.query(Hotel)
    session.close()
    return hotels_query.all()


if __name__ == "__main__":
    hotels = query_hotels()
    if len(hotels) == 0:
        populate_database()
