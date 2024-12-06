from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium import webdriver


@given('I open the url "{url}')
def get_url(context, url):
    context.behave_driver.get(url)


@when('I input "{value}" for side "{side}"')
def step_input_side(context, value, side):
    input_field = context.behave_driver.find_element(By.ID, side)
    input_field.clear()
    input_field.send_keys(value)




@when('I click the "Calculate" button')
def step_click_calculate_button(context):
    calculate_button = context.behave_driver.find_element(By.CLASS_NAME, "clcbtn")
    calculate_button.click()


@then('I should see the area "{expected_area}"')
def step_verify_area(context, expected_area):
    result_field = context.behave_driver.find_element(By.ID, "_d")
    actual_area = result_field.get_attribute("value") 
    assert actual_area == expected_area, f"Expected area {expected_area}, but got {actual_area}"