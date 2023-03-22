Feature: Check the SignIn Page functionality

  Background:
    Given login: I am a user on the login page
    When sign_up: I am a user on the Sign up page


   @sign
    Scenario: Enter credentials and check them
    When sign_up: I click on the sign up button
    When sign_up: I click on the BUSINESS button
    When sign_up: I click on the PERSONAL button
    When sign_up: I click on the CONTINUE button
    When sign_up: I fill in Enter your first name "Laura"
    When sign_up: I press Enter after I whrite my first name
    When sign_up: I fill in Add your last name "Popa"
    When sign_up: I press Enter after I whrite my last name
    When sign_up: I fill in your email, a wrong email "laurayahoo.com"
    When sign_up: I verify the error message "Please enter a valid email address."
    When sign_up: I clear the email wrong
    When sign_up: I fill in your email, my email "popa_laura@yahoo.com"
    When sign_up: I press Enter after I whrite my email
    When sign_up: I fill in your password "Parola-123"
    Then sign_up: I press Enter after I whrite my password