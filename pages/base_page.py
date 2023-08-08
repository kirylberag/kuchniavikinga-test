from selenium.webdriver.chrome.webdriver import WebDriver
import allure


@allure.feature('Base page')
class BasePage:
    base_url = 'kuchniavikinga.pl'
    beginning_url = None
    page_url = None
    list_elements = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Open page')
    def open_page(self):
        if self.page_url:
            self.driver.get(f'https://{self.beginning_url}{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError("No no no, can't open")

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)
