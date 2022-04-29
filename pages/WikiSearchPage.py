from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class WikiSearchPage(BasePage):
    did_u_mean_suggestion = (By.XPATH, "//div[text()= 'Did you mean: ']/a")
    suggestion = (By.XPATH, "//li[@class='mw-search-result']/div/a")
    search_page = (By.XPATH, "//h1[text()='Search results']/following::input[@id='ooui-php-1']")
    did_you_mean_suggestion = (By.XPATH, "//div[text()='Did you mean: ']/a")

    def __init__(self, driver):
        super().__init__(driver)

    def verify_did_u_mean_suggestion_is_visible(self):
        return self.is_visible(self.did_u_mean_suggestion)

    def get_suggestion_count(self):
        return str(len(self.get_elements(self.suggestion)))

    def click_search_suggestion(self, sequence):
        suggestion_text = self.get_text_and_click(self.get_elements(self.suggestion)[sequence])
        return suggestion_text

    def verify_search_result_page(self, search_key):
        return self.get_attribute_value(self.search_page, "value") == search_key

    def click_did_you_mean_suggestion(self):
        self.click(self.did_u_mean_suggestion)
