from auto_practice.pages.base import BasePage
import auto_practice.helpers.user_generator as user_gen
from auto_practice.locators.demo_form_locators import DemoLocators, DatePicker


class FormPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.demo_locators = DemoLocators()
        self.date_picker_locators = DatePicker()
        self.user = user_gen.make_user()

    def open_and_wait_for_load(self):
        self.navigate_to()
        self.get_element(self.demo_locators.current_address)
        self.remove_ad_footer()

    def fill_form(self):
        dl = self.demo_locators
        self.get_element(dl.first_name).send_keys(self.user.first_name)
        self.get_element(dl.last_name).send_keys(self.user.last_name)
        self.get_element(dl.mobile_number).send_keys(self.user.mobile)
        self.get_element(dl.email).send_keys(self.user.email)
        self.get_element(getattr(dl, "gender_"+self.user.gender)).click()

    def submit_form(self):
        self.get_element(self.demo_locators.submit_btn).click()
        self.get_elements(self.demo_locators.result_table)

    def fill_dob(self):
        # separate method for dob, react datepicker is a little tricky
        dl = self.demo_locators
        dp = self.date_picker_locators
        dob = self.user.dob
        year = dob.strftime("%Y")
        month = dob.strftime("%B")
        day = dob.strftime("%e")

        self.get_element(dl.dob).click()
        self.select_value(dp.month_selector, month, how='visible_text')
        self.select_value(dp.year_selector, year, how='visible_text')
        selected_month = self.get_elements(dp.day_selector)
        # because %e adds ' '  in single digit days and breaks filter
        # first select days of month, because picker displays last week of prev. month and fist week of next one
        month_days = list(filter(lambda x: month in x.get_attribute('aria-label'), selected_month))
        # then select day, still could be refactored
        day = list(filter(lambda x: day in x.get_attribute('aria-label'), month_days))[0]
        day.click()

    def save_result(self) -> dict:
        def process_elements(locator: tuple) -> list:
            elements = self.get_elements(locator)
            data = [i.text for i in elements]
            return data

        table_values = process_elements(self.demo_locators.result_table)
        table_keys = process_elements(self.demo_locators.result_table_keys)
        table_data = dict(zip(table_keys, table_values))

        self.get_element(self.demo_locators.close_table).click()

        return table_data



