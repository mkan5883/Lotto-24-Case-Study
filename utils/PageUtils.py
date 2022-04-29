from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageUtils:
    def __init__(self, driver):
        self.driver = driver

    def get_elements(self, locator):
        method = locator[0]
        value = locator[1]
        return self.driver.find_elements(method, value)

    def get_element(self, locator):
        method = locator[0]
        value = locator[1]
        return self.driver.find_element(method, value)

    def is_visible(self, locator):
        try:
            self.get_element(locator).is_displayed()
            return True
        except NoSuchElementException:
            return False

    def wait_visible(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return element

    def wait_till_element_visible(self, element):
        WebDriverWait(self.driver, 20).until(EC.visibility_of(element))

    def wait_clickable(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        return element

    def click(self, locator):
        element = self.wait_clickable(locator)
        element.click()

    def get_text_and_click_element(self, element):
        self.wait_till_element_visible(element)
        txt = element.text
        element.click()
        return txt

    def get_text(self, locator):
        element = self.wait_visible(locator)
        return element.text

    def send_keys(self, locator, text):
        element = self.wait_clickable(locator)
        element.click()
        element.send_keys(text)
        sleep(0.5)

    def get_attribute_value(self, locator, value):
        element = self.wait_visible(locator)
        return element.get_attribute(value)
