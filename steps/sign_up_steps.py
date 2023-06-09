from behave import *

@when('sign_up: I am a user on the Sign up page')
def step_impl(context):
    context.sign_up_page.navigate_to_sign_up_page()

@when('sign_up: I test if the url is correct')
def step_impl(context):
    context.sign_up_page.test_url()

@when('sign_up: I test if the title of the page is correct')
def step_impl(context):
    context.sign_up_page.test_page_title()

@when('sign_up: I click on the sign up button')
def step_impl(context):
    context.sign_up_page.sign_up()


@when('sign_up: I test the Bussiness button and Personal button')
def step_impl(context):
    context.sign_up_page.click_radio_button()

@when('sign_up: I click on the CONTINUE button')
def step_impl(context):
    context.sign_up_page.continue_button()

@when ('sign_up: I test if the first name is "{first_name}"')
def step_impl(context, first_name):
    context.sign_up_page.test_first_name(first_name)

@when('sign_up: I press Enter after I whrite my first name')
def step_impl(context):
    context.sign_up_page.enter_after_first_name()

@when('sign_up: I test if the last name is "{last_name}"')
def step_impl(context, last_name):
    context.sign_up_page.test_last_name(last_name)

@when('sign_up: I press Enter after I whrite my last name')
def step_impl(context):
    context.sign_up_page.enter_after_last_name()

@when('sign_up: I fill in your email, a wrong email "{wrong}"')
def step_impl(context, wrong):
    context.sign_up_page.enter_wrong_email(wrong)

@when('sign_up: I test the error message "{msg}"')
def step_impl(context, msg):
    context.sign_up_page.test_error(msg)

@when('sign_up: I clear the email wrong')
def step_impl(context):
    context.sign_up_page.clear_email_input()

@when('sign_up: I fill in your email, my email "{email}"')
def step_impl(context, email):
    context.sign_up_page.email_field(email)

@when('sign_up: I test if the error is not displayed anymore')
def step_impl(context):
    context.sign_up_page.test_error_is_not_displayed_anymore()


@when('sign_up: I press Enter after I whrite my email')
def step_impl(context):
    context.sign_up_page.enter_after_email_field()

@when('sign_up: I fill in your password "{password}"')
def step_impl(context, password):
    context.sign_up_page.password_field(password)

@when('sign_up: I press Enter after I whrite my password')
def step_impl(context):
    context.sign_up_page.enter_after_password_field()

@then('sign_up: I test if url logout is egal with url login')
def step_impl(context):
    context.sign_up_page.test_url_dupa_delogare()
