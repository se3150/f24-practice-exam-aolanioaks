from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium import webdriver


# <div class="mathquill-embedded-latex mathquill-rendered-math"><span class="text">Enter the length of <b>&#8216; a &#8216;</b> =</span><input id="a" class="oInp" size="3" type="text" /></p>
# <p><span class="text">Enter the length of <b>&#8216; b &#8216;</b> =</span><input id="b" class="oInp" size="3" type="text" /></p>
# <p><span class="text">Enter the length of <b>&#8216; c &#8216;</b> =</span><input id="c" class="oInp" size="3" type="text" /></p>
# <p><span class="text">Semi Perimeter =</span><input id="_e" class="oInp oOutp" disabled="disabled" size="3" type="text" /></p>
# <p><input class="clcbtn" type="button" value="Calculate" /></p>
# <p><span class="text">The area of triangle (A) =</span><input id="_d" class="oInp oOutp" disabled="disabled" size="3" type="text" /></div>


@given('I open the url "{url}')
def get_url(context, url):
    context.behave_driver.get(url)


@when('I input "{number}" for side "{side}"')
def step_input_side(context, number, side):
    input_field = context.behave_driver.find_element(By.ID, side)
    input_field.send_keys(number)



@when('I click the "Calculate" button')
def step_click_calculate_button(context):
    calculate_button = context.behave_driver.find_element(By.CLASS_NAME, "clcbtn")
    calculate_button.click()


@then('I should see the area "{expected_area}"')
def step_verify_area(context, expected_area):
    result_field = context.behave_driver.find_element(By.ID, "_d")
    actual_area = result_field.get_attribute("value") 
    assert actual_area == expected_area