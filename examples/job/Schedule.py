import schedule

from ..service.ShopeeCrawler import ShopeeCrawler
from ..service.LazadaCrawler import LazadaCrawler
from ..base.base import session_factory


class Schedule:
    def job():
        session = session_factory()

        session.execute('''TRUNCATE TABLE product RESTART IDENTITY''')

        session.commit()
        session.close()

        print('Xóa dữ liệu trước khi quét')

        ShopeeCrawler.craw()
        LazadaCrawler.craw()

    schedule.every().hour.at(':00').do(job)

    def run(self):
        while 1:
            schedule.run_pending()
