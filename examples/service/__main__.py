from .ShopeeCrawler import ShopeeCrawler
from .LazadaCrawler import LazadaCrawler
from ..base.base import session_factory

session = session_factory()

session.execute('''TRUNCATE TABLE product RESTART IDENTITY''')

session.commit()
session.close()

print('Xóa dữ liệu trước khi quét')

ShopeeCrawler.craw()
LazadaCrawler.craw()
