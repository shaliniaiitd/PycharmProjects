from framework.ui.base.base_page import BasePage


class HomePage(BasePage):
    img_github_fork_image = "xpath|//img"

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def click_img_github_fork_image(self):
        # This is the function to perform click on web element img_github_fork_image
        self.do.click(self.img_github_fork_image)
        return self

    def double_click_img_github_fork_image(self):
        # This is the function to perform doubleClick on web element img_github_fork_image
        self.do.double_click(self.img_github_fork_image)
        return self

    def get_attribute_img_github_fork_image(self, attribute):
        # This is the function to perform getAttribute on web element img_github_fork_image
        return self.do.get_attribute(self.img_github_fork_image, attribute)


