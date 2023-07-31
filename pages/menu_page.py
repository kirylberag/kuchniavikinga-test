from pages.base_page import BasePage
from locators import menu_page_locators as MPL
import datetime


class MenuPage(BasePage):
    page_url = '/menu'

    @property
    def page_title(self):
        return self.driver.title

    def day_on_page(self, difference=None):
        if difference:
            day = self.find_all(MPL.day_today)[7 + difference].get_attribute('innerText')
        else:
            day = self.find_all(MPL.day_today)[7].get_attribute('innerText')
        answer = {
            'Poniedziałek': 'Monday',
            'Wtorek': 'Tuesday',
            'Środa': 'Wednesday',
            'Czwartek': 'Thursday',
            'Piątek': 'Friday',
            'Sobota': 'Saturday',
            'Niedziela': 'Sunday'
        }
        return answer[day]

    @property
    def day_real(self):
        date_now = datetime.datetime.now()
        return date_now.strftime('%A')

    def date_on_page(self, difference=None):
        if difference:
            date = self.find_all(MPL.date_today)[7 + difference].get_attribute('innerText')
        else:
            date = self.find_all(MPL.date_today)[7].get_attribute('innerText')
        return date

    @property
    def date_real(self):
        date_now = datetime.datetime.now()
        return date_now.strftime('%d/%m/%Y')

    def three_clicks_glide_arrow_left(self):
        for i in range(3):
            self.find(MPL.glide_arrow_left).click()

    def two_clicks_glide_arrow_right(self):
        for i in range(2):
            self.find(MPL.glide_arrow_right).click()

    def click_field_menu(self):
        self.find(MPL.button_menu_choice).click()

    def click_menu_summer_vibes(self):
        self.find(MPL.button_summer_vibes).click()

    def click_menu_ladies_vibes(self):
        self.find(MPL.button_ladies_vibes).click()

    def click_menu_standard(self):
        self.find(MPL.button_standard).click()

    def click_menu_active_pro(self):
        self.find(MPL.button_active_pro).click()

    def click_menu_low_ig(self):
        self.find(MPL.button_low_ig).click()

    def click_menu_ketogeniczna(self):
        self.find(MPL.button_ketogeniczna).click()

    def click_menu_soft(self):
        self.find(MPL.button_soft).click()

    def click_menu_made_by_chef(self):
        self.find(MPL.button_made_by_chef).click()

    def click_menu_ekonomiczna(self):
        self.find(MPL.button_ekonomiczna).click()

    def click_menu_bez_laktozy_i_glutenu(self):
        self.find(MPL.button_bez_laktozy_i_glutenu).click()

    def click_menu_wege_ryby(self):
        self.find(MPL.button_wege_ryby).click()

    def click_menu_ekonomiczna_wege(self):
        self.find(MPL.button_ekonomiczna_wege).click()

    def click_menu_hashimoto(self):
        self.find(MPL.button_hashimoto).click()

    def click_menu_weganska(self):
        self.find(MPL.button_weganska).click()

    def click_menu_progress(self):
        self.find(MPL.button_progress).click()

    def click_menu_fodmap(self):
        self.find(MPL.button_fodmap).click()

    def meals(self, dieta=None):
        all_diets = {
            'meals_summer_vibes': MPL.meals_summer_vibes,
            'meals_ladies_vibes': MPL.meals_ladies_vibes,
            'meals_standard': MPL.meals_standard,
            'meals_active_pro': MPL.meals_active_pro,
            'meals_low_ig': MPL.meals_low_ig,
            'meals_ketogeniczna': MPL.meals_ketogeniczna,
            'meals_soft': MPL.meals_soft,
            'meals_made_by_chef': MPL.meals_made_by_chef,
            'meals_ekonomiczna': MPL.meals_ekonomiczna,
            'meals_bez_laktozy_i_glutenu': MPL.meals_bez_laktozy_i_glutenu,
            'meals_wege_ryby': MPL.meals_wege_ryby,
            'meals_ekonomiczna_wege': MPL.meals_ekonomiczna_wege,
            'meals_hashimoto': MPL.meals_hashimoto,
            'meals_weganska': MPL.meals_weganska,
            'meals_progress': MPL.meals_progress,
            'meals_fodmap': MPL.meals_fodmap
        }
        menu = self.find_all(all_diets[dieta])
        meals = list()
        for element in menu:
            meal = element.get_attribute('innerText')
            if meal not in meals:
                meals.append(meal)
            else:
                break
        return meals

    def click_logo(self):
        self.find_all(MPL.button_logo)[0].click()
