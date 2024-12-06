Feature: calculate the area of a triangle
As an aspiring mathematician
I should be able to calculate the area of a triangle
So that I can chat with my math friends like a pro

Scenario: I can calculate the area of a triangle
    Given I open the url "https://byjus.com/herons-calculator/"
    When I input "5" for side "a"
    And I input "12" for side "b"
    And I input "13" for side "c"
    And I click the "Calculate" button
    Then I should see the area "30"