from ui_pytest.pageobjects.actions.HomePage import HomePage


class HomePageVerification(HomePage):
    def __init__(self, driver):
        super(HomePageVerification, self).__init__(driver)

    def is_present_img_github_fork_image(self):
        # This is the function to perform verifyIsElementPresent on web element img_github_fork_image
        return self.verify.is_present(self.img_github_fork_image)


