from sqlalchemy import Column, String, Integer, ForeignKey, Numeric
from ..base.base import Base


class Hotel(Base):
    __tablename__ = 'hotel'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    minPrice = Column(Numeric(20,2))
    maxPrice = Column(Numeric(20,2))
