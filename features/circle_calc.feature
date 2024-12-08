Feature: I visit the Circle Area Calculator
    I want to learn how to graph a circle
    So I can chat with my friends about it 



Scenario: I can use a circle area calculator
    Given I open the url "https://byjus.com/area-of-a-circle-calculator/"
    When I input "10" in the "radius"
    And I click the calculate button
    Then I should see the area to be "314.159"
    