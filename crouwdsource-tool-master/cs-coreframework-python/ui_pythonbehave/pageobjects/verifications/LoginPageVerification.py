from ui_pythonbehave.pageobjects.actions.LoginPage import LoginPage


class LoginPageVerification(LoginPage):
    def __init__(self, driver):
        super(LoginPageVerification, self).__init__(driver)

    def is_present_tb_username(self):
        # This is the function to perform verifyIsElementPresent on web element tb_username
        return self.verify.is_present(self.tb_username)

    def is_present_tb_password(self):
        # This is the function to perform verifyIsElementPresent on web element tb_password
        return self.verify.is_present(self.tb_password)

    def is_present_btn_login(self):
        # This is the function to perform verifyIsElementPresent on web element btn_login
        return self.verify.is_present(self.btn_login)


