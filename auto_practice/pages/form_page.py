from auto_practice.pages.base import BasePage
from auto_practice.helpers.user import User
import auto_practice.helpers.user_generator as user_gen
from auto_practice.locators.demo_form_locators import DemoLocators, DatePicker


class FormPage(BasePage):
    # may be this is not the best way, refactor classes?
    demo_locators = DemoLocators()
    date_picker_locators = DatePicker()
    user = user_gen.make_user()

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
        month_elements = list(filter(lambda x: month in x.get_attribute('aria-label'), selected_month))
        day = list(filter(lambda x: day in x.get_attribute('aria-label'), month_elements))[0]
        day.click()

    def save_result(self) -> dict:
        #This needs to be refactored, to much repetition
        table_data_elements = self.get_elements(self.demo_locators.result_table)
        table_data_keys = self.get_elements(self.demo_locators.result_table_keys)
        table_values = [i.text for i in table_data_elements]
        table_keys = [i.text for i in table_data_keys]
        table_data = dict(zip(table_keys, table_values))
        self.get_element(self.demo_locators.close_table).click()
        return table_data

    def compare_user(self, expected: User, actual: dict) -> bool:
        user = expected.to_dict()
        # not the best way but will do
        return user == actual

