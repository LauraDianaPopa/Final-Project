Feature: Check the Login Page functionality

  Background:
    Given login: I am a user on the login page

    @rong_email
    Scenario: Check if you forgot the password
    When login: I fill in Enter your email "popa_laura_diana@yahoo.com"
    When login: I fill a rong password in the fill Enter your password "abs"
    When login: I click on the log in button
    When login: I click Forgot password?
    When login: I fill in Enter your email "popa_laura_diana@yahoo.com"
    When login: I click SEND EMAIL
    When login: I check de validation message

    @email
    Scenario: Check the login page when I enter my email and password
    When login: I fill in Enter your email "popa_laura_diana@yahoo.com"
    When login: I fill in Enter your password "parola01"
    When login: I click on the log in button





