from .CrawService import CrawService
from requests_html import HTML
from ..base.base import session_factory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ..models.product import Product


class ShopeeCrawler():
    def craw():
        session = session_factory()

        craw_service = CrawService()

        # CRAW DATA FROM SHOPEE
        url = 'https://shopee.vn'
        browser = craw_service.craw_html(url)
        delay = 5
        WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, '_2o2XQg')))

        html_has_category = HTML(html=browser.page_source)
        categories = html_has_category.find('._2o2XQg')
        for category in categories:
            # save category to database
            category_url = url + category.links.pop()
            browser_category = craw_service.craw_html(category_url)
            delay = 5
            WebDriverWait(browser_category, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'customized-overlay-image')))
            html_has_products = HTML(html=browser_category.page_source)
            products_html = html_has_products.find('.shopee-search-item-result__item')
            for product_html in products_html:
                product_name_html = product_html.find('.yQmmFK')
                lowest_price_html = product_html.find('.WTFwws ._24JoLh')
                highest_price_html = product_html.find('.WTFwws ._24JoLh:last-child')
                image_html = product_html.find('img')
                url_html = product_html.find('a')
                if (product_name_html.__len__() > 0
                        or lowest_price_html.__len__() > 0
                        or highest_price_html.__len__() > 0
                        or url_html.__len__() > 0):
                    product_name = product_name_html[0].text
                    lowest_price = float(lowest_price_html[0].text.replace('.', ''))
                    highest_price = float(highest_price_html[0].text.replace('.', ''))
                    product_url = url + url_html[0].attrs.get('href')

                    product = Product()

                    product.name = product_name
                    product.url = product_url
                    product.minPrice = lowest_price
                    product.maxPrice = highest_price

                    if image_html.__len__() > 0:
                        image = image_html[0].attrs.get('src')
                        product.image=image

                    session.add(product)
                    session.commit()
        # END CRAW DATA FROM SHOPEE

        browser.close()
        print('Quét dữ liệu đã hoàn tất')
        session.close()
