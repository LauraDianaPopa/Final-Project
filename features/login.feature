Feature: Check the Login Page functionality

  Background:
    Given login: I am a user on the login page

    @email
    Scenario: Check the login page when I enter my email and password
    When login: I fill in Enter your email "popa_laura_diana@yahoo.com"
    When login: I fill in Enter your password "parola01"
    When login: I click on the log in button





