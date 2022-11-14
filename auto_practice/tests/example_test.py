from auto_practice.pages.form_page import FormPage


def test_form(driver):
    fp = FormPage(driver, "https://demoqa.com/automation-practice-form")
    fp.open_and_wait_for_load()
    fp.fill_form()
    fp.fill_dob()
    fp.submit_form()
    user = fp.user
    result = fp.save_result()
    assert fp.compare_user(user, result) == True
