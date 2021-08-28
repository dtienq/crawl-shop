from .CrawService import CrawService
from requests_html import HTML
from ..models.craw_html import CrawHTML
from ..base.base import session_factory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

session = session_factory()

craw_service = CrawService()

# craw html data from shopee
url='https://shopee.vn'
browser = craw_service.craw_html(url)
delay=3
WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, '_2o2XQg')))


html_has_category = HTML(html=browser.page_source)
categories=html_has_category.find('._2o2XQg')
for category in categories:
    # save category to database
    category_url=url + category.links.pop()
    browser = craw_service.craw_html(category_url)
    delay = 3
    WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'customized-overlay-image')))
    html_has_products=HTML(html=browser.page_source)
    products=html_has_products.find('.shopee-search-item-result__item')
    for product in products:
        print(product.find('.yQmmFK'))



session.commit()
session.close()
