from sqlalchemy import Column, String, Integer, ForeignKey, Numeric
from ..base.base import Base


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    minPrice = Column(Numeric(20,2))
    maxPrice = Column(Numeric(20,2))
    image = Column(String)
