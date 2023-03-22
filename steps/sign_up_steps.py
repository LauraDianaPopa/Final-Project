from behave import *

@when('sign_up: I am a user on the Sign up page')
def step_impl(context):
    context.sign_up_page.navigate_to_sign_up_page()

@when('sign_up: I click on the sign up button')
def step_impl(context):
    context.sign_up_page.sign_up()

@when('sign_up: I click on the BUSINESS button')
def step_impl(context):
    context.sign_up_page.business_button()

@when('sign_up: I click on the PERSONAL button')
def step_impl(context):
    context.sign_up_page.personal_button()

@when('sign_up: I click on the CONTINUE button')
def step_impl(context):
    context.sign_up_page.continue_button()

@when ('sign_up: I fill in Enter your first name "{first_name}"')
def step_impl(context, first_name):
    context.sign_up_page.first_name_field(first_name)

@when('sign_up: I press Enter after I whrite my first name')
def step_impl(context):
    context.sign_up_page.enter_after_first_name()

@when('sign_up: I fill in Add your last name "{last_name}"')
def step_impl(context, last_name):
    context.sign_up_page.last_name_field(last_name)

@when('sign_up: I press Enter after I whrite my last name')
def step_impl(context):
    context.sign_up_page.enter_after_last_name()

@when('sign_up: I fill in your email, a wrong email "{wrong}"')
def step_impl(context, wrong):
    context.sign_up_page.enter_wrong_email(wrong)

@when('sign_up: I verify the error message "{msg}"')
def step_impl(context, msg):
    context.sign_up_page.verify_error(msg)

@when('sign_up: I clear the email wrong')
def step_impl(context):
    context.sign_up_page.clear_email_input()

@when('sign_up: I fill in your email, my email "{email}"')
def step_impl(context, email):
    context.sign_up_page.email_field(email)

@when('sign_up: I verify if the error is not displayed anymore')
def step_impl(context):
    context.sign_up_page.verify_error_is_not_displayed_anymore()


@when('sign_up: I press Enter after I whrite my email')
def step_impl(context):
    context.sign_up_page.enter_after_email_field()

@when('sign_up: I fill in your password "{password}"')
def step_impl(context, password):
    context.sign_up_page.password_field(password)

@then('sign_up: I press Enter after I whrite my password')
def step_impl(context):
    context.sign_up_page.enter_after_password_field()
