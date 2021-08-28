from sqlalchemy import Column, Integer, String, Text
from ..base.base import Base


class CrawHTML(Base):
    __tablename__ = 'craw_html'

    id = Column(Integer, primary_key=True)
    html = Column(Text, nullable=False)
    web_url = Column(String, nullable=False)
