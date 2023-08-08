from pages.base_page import BasePage
import allure


@allure.feature('Other page')
class OtherPage(BasePage):
    page_url = None

    @property
    @allure.step('Display page title')
    def page_title(self):
        return self.driver.title
