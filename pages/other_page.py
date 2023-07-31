from pages.base_page import BasePage


class OtherPage(BasePage):
    page_url = None

    @property
    def page_title(self):
        return self.driver.title
