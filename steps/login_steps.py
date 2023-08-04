from behave import *




@given('login: I am a user on the login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when('login: I fill in Enter your email "{email}"')
def step_impl(context,email):
    context.login_page.email_field(email)

@when ('login: I fill a rong password in the fill Enter your password "{rong_pass}"')
def step_impl(context, rong_pass):
    context.login_page.rong_password(rong_pass)

@when ('login: I click on the log in button')
def step_impl(context):
    context.login_page.login_button1()

@when ('login: I click Forgot password?')
def step_impl(context):
    context.login_page.forgot_link()

@when ('login: I fill in Enter your email "{email}"')
def step_impl(context, email):
    context.login_page.email_field_1(email)

@when('login: I click SEND EMAIL')
def step_impl(context):
    context.login_page.send_email()

@when('login: I fill in Enter your email "{email}"')
def step_impl(context, email):
    context.login_page.email_field_2(email)

@when('login: I fill in Enter your password "{password}"')
def step_impl(context, password):
    context.login_page.password_field(password)

@when('login: I click on the log in button')
def step_impl(context):
    context.login_page.login_button()



