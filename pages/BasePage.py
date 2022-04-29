from utils.PageUtils import PageUtils


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.page_utils = PageUtils(self.driver)

    def get_element(self, locator):
        return self.page_utils.get_element(locator)

    def get_elements(self, locator):
        return self.page_utils.get_elements(locator)

    def is_visible(self, locator):
        return self.page_utils.is_visible(locator)

    def wait_visible(self, locator):
        self.page_utils.wait_visible(locator)

    def click(self, locator):
        self.page_utils.click(locator)

    def get_text_and_click(self, element):
        return self.page_utils.get_text_and_click_element(element)

    def get_text(self, locator):
        return self.page_utils.get_text(locator)

    def send_keys(self, locator, text):
        self.page_utils.send_keys(locator, text)

    def get_attribute_value(self, locator, value):
        return self.page_utils.get_attribute_value(locator, value)
