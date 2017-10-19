Feature: Admin Login
  Scenario: Admin user logs in with correct credentials
    Given Admin user has correct credentials
    When Admin opens the browser
    And Admin user enters his user name
    And Admin user enters his password
    And Admin user clicks on the login button
    Then Admin user should be taken to the login page