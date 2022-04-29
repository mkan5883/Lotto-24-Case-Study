from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ArticlePage(BasePage):
    article_title = (By.ID, "firstHeading")

    def __init__(self, driver):
        super().__init__(driver)

    def get_article_title(self):
        return self.get_text(self.article_title)
