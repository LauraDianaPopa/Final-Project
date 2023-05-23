from behave import *




@given('login: I am a user on the login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when('login: I fill in Enter your email "{email}"')
def step_impl(context,email):
    context.login_page.email_field(email)

@when('login: I fill in Enter your password "{password}"')
def step_impl(context, password):
    context.login_page.password_field(password)

@when('login: I click on the log in button')
def step_impl(context):
    context.login_page.login_button()



