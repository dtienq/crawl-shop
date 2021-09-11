from selenium import webdriver

class CrawService:
    def craw_html(self, url):
        browser = webdriver.Chrome(executable_path='chromedriver.exe')
        browser.get(url)
        return browser
