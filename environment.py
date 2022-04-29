import platform
from selenium import webdriver

from pages.WikiHomePage import WikiHomePage
from pages.WikiSearchPage import WikiSearchPage
from pages.ArticlePage import ArticlePage


def before_all(context):
    if platform.system() == 'Windows':
        context.executable_path = '\\chromedriver.exe'
    else:
        context.executable_path = './chromedriver'

    context.driver = webdriver.Chrome(executable_path=context.executable_path)
    context.driver.maximize_window()
    context.home_page = WikiHomePage(context.driver)
    context.search_page = WikiSearchPage(context.driver)
    context.article_page = ArticlePage(context.driver)


def after_all(context):
    print('-----------------END-----------------')
    context.driver.close()
