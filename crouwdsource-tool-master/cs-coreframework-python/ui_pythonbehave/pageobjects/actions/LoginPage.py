from framework.ui.base.base_page import BasePage


class LoginPage(BasePage):
    tb_username = "id|username"
    tb_password = "xpath|//input[@name='password']"
    btn_login = "xpath|//input[@name='login']"

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def input_text_tb_username(self, text):
        # This is the function to perform setText on web element tb_username
        self.do.input_text(self.tb_username, text)
        return self

    def input_text_tb_password(self, text):
        # This is the function to perform setText on web element tb_password
        self.do.input_text(self.tb_password, text)
        return self

    def click_btn_login(self):
        # This is the function to perform click on web element btn_login
        self.do.click(self.btn_login)
        return self


