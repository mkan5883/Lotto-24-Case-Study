from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class WikiHomePage(BasePage):
    home_page_title = (By.ID, "Welcome_to_Wikipedia")
    search_box = (By.ID, "searchInput")
    search_button = (By.ID, "searchButton")

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self):
        return self.get_text(self.home_page_title)

    def enter_search_keyword(self, search_key):
        self.send_keys(self.search_box, search_key)

    def click_search_button(self):
        self.click(self.search_button)
