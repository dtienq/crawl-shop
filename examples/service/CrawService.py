from selenium import webdriver

class CrawService:
    def craw_html(self, url):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        browser = webdriver.Chrome(executable_path='chromedriver.exe', options=option)
        browser.get(url)
        return browser
