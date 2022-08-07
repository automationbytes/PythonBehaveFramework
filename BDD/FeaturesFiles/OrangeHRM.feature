@Regression
Feature: OrangeHRM Testcases

  Scenario: OrangeHRM Login

    Given the user launches Application
    Then the user verifies logo
    When the user enters username in username field
    Then the user enters password in password field
    And the user clicks on login button

  Scenario: OrangeHRM Logout
    When the user verifies home Page title
    Then the user clicks on logout button