from .CrawService import CrawService
from requests_html import HTML
from ..base.base import session_factory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ..models.product import Product


class LazadaCrawler():
    def craw():
        try:
            session = session_factory()

            craw_service = CrawService()

            # CRAW DATA FROM LAZADA
            url = 'https://lazada.vn'
            browser = craw_service.craw_html(url)
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            delay = 5
            WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'card-jfy-li-content')))

            html_has_category = HTML(html=browser.page_source)

            products_home_html = html_has_category.find('.card-jfy-item-wrapper')

            # get product on home page
            for product_html in products_home_html:
                product_name = product_html.find('.card-jfy-title')[0].text
                price = float(product_html.find('.price')[0].text.replace(',', '').replace('.', ''))
                product_url = product_html.find('a')[0].attrs.get('href')
                image = product_html.find('img')[0].attrs.get('src')

                product = Product()

                product.name = product_name
                product.url = product_url
                product.minPrice = price
                product.maxPrice = price
                product.image = image

                session.add(product)

            # END CRAW DATA FROM LAZADA

            # browser.close()
            print('Quét dữ liệu đã hoàn tất')
            session.commit()
            session.close()
        except:
            LazadaCrawler.craw()
