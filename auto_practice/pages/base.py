from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys

class BasePage:
    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url

    def navigate_to(self):
        self.driver.get(self.url)

    def get_element(self, locator: tuple, timeout=5):
        return WebDriverWait(self.driver, timeout)\
            .until(EC.visibility_of_element_located(locator), ' : '.join(locator))

    def get_elements(self, locator: tuple, timeout=5):
        return WebDriverWait(self.driver, timeout)\
            .until(EC.visibility_of_any_elements_located(locator), ' : '.join(locator))

    def remove_ad_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('fixedban').style.display='none'")


    def select_value(self,selector_loc: tuple,value, how='value'):
        selector = Select(self.get_element(selector_loc))
        if how=='value':
            selector.select_by_value(value)
        elif how=='visible_text':
            selector.select_by_visible_text(value)


    def send_return_key(self,loc: tuple):
        self.get_element(loc).send_keys(Keys.RETURN)
