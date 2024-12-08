from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium import webdriver



@given('I open the url "{url}"')
def I_open_the_url(context, url):
    context.behave_driver.get(url)



@when('I input "{value}" in the "{x}"')
def I_input_10_on_radius(context, value, x):
    input_field = context.behave_driver.find_element(By.ID, "x")
    input_field.send_keys(value)


@when('I click the calculate button')
def I_click_calculate_button(context):
    click_button = context.behave_driver.find_element(By.CLASS_NAME, "clcbtn")
    click_button.click()




@then('I should see the area to be "{expected_value}"')
def I_get_should_see_the_area(context, expected_value):
    result = context.behave_driver.find_element(By.ID, "_answer")
    actual_area = result.get_attribute("value")
    assert actual_area == expected_value
    