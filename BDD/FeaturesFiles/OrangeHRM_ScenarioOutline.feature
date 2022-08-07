Feature: OrangeHRM Testcases
  @Sanity
  Scenario Outline: OrangeHRM Login i wht Scenario Outline

    Given the user launches Application
    Then the user verifies logo
    When the user enters "<username>" in username field
    Then the user enters "<password>" in password field
    And the user clicks on login button
    Examples:
      |username|password|
      |admin   |admin123|
      |abcd    |abcd123 |
      |admin    |abcd123 |
      |#a$ag    |abcd123 |


