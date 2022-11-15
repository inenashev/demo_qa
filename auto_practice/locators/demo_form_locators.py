from selenium.webdriver.common.by import By


class DemoLocators:

    first_name = (By.CSS_SELECTOR, "#firstName")
    last_name = (By.CSS_SELECTOR, "#lastName")
    email = (By.CSS_SELECTOR, "#userEmail")
    mobile_number = (By.CSS_SELECTOR, "#userNumber")
    dob = (By.CSS_SELECTOR, "#dateOfBirthInput")
    subject = (By.CSS_SELECTOR, "#subjectsInput")
    upload_picture = (By.CSS_SELECTOR, "#uploadPicture")
    current_address = (By.CSS_SELECTOR, "#currentAddress")

    gender_selector = (By.CSS_SELECTOR, "#genterWrapper")
    gender_male = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    gender_female = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    gender_other = (By.CSS_SELECTOR, "label[for='gender-radio-3']")

    hobbies_selector = (By.CSS_SELECTOR, "#hobbiesWrapper")
    hobbies_sports = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    hobbies_reading = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
    hobbies_music = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")

    select_state = (By.CSS_SELECTOR, "#state")

    def select_state_value(self, value: str) -> tuple:
        valid_states = ['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']
        if value in valid_states:
            return (By.XPATH,f"//div[contains(text(),'{value}')]")
        else:
            raise ValueError("State is not valid")

    select_city = (By.CSS_SELECTOR, "#city")

    def select_city_value(self, value: str) -> tuple:
        valid_cities = ['Agra', 'Lucknow', 'Merrut']
        if value in valid_cities:
            return (By.XPATH,f"//div[contains(text(),'{value}')]")
        else:
            raise ValueError("City is not valid")

    submit_btn = (By.CSS_SELECTOR, '#submit')

    result_table = (By.XPATH, '//div[@class="table-responsive"]//td[2]')
    result_table_keys = (By.XPATH, '//div[@class="table-responsive"]//td[1]')
    close_table = (By.CSS_SELECTOR, "#closeLargeModal")


class DatePicker:

    date_picker = (By.CSS_SELECTOR, ".react-datepicker")
    month_selector = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    year_selector = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    selected_month = (By.CSS_SELECTOR, ".react-datepicker__month")
    day_selector = (By.CSS_SELECTOR,'.react-datepicker__day')
