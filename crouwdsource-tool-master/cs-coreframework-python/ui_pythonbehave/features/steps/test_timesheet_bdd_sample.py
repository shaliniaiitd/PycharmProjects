from behave import given, when, then
from framework.core.utils.logger_factory import LoggerFactory


logger = LoggerFactory.get_logger("TEST")

# Given Steps

@given('the Timesheet home page is displayed')
def timesheet_home(context):
    context.pages.login.open_url(context.pages.base_url)

# When Steps
@when('the user enter username as "{username}" and password as "{password}" and clicks login')
def login(context, username,password):
    context.pages.login.input_text_tb_username(username)
    context.pages.login.input_text_tb_password(password)
    context.pages.login.click_btn_login()


# Then Steps
@then('user should be navigated to welcome page')
def user_logged_in(context):
    assert context.pages.home_verify.is_text_link_welcome_username("clbuser1")