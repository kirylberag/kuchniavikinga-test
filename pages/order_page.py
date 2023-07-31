from pages.base_page import BasePage
from locators import order_page_locators as OPL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import datetime
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import random
from time import sleep


class OrderPage(BasePage):
    page_url = '/zamowienie/'
    beginning_url = '//zamow.'

    @property
    def page_title(self):
        return self.driver.title

    @property
    def url_page(self):
        return self.driver.current_url

    def click_step_button_choice_diet(self):
        self.find_all(OPL.step_order)[0].click()

    def click_step_button_choice_date(self):
        self.find_all(OPL.step_order)[1].click()

    def click_step_button_choice_add(self):
        self.find_all(OPL.step_order)[2].click()

    def click_step_button_choice_cart(self):
        self.find_all(OPL.step_order)[3].click()

    def click_step_button_choice_data(self):
        self.find_all(OPL.step_order)[4].click()

    def click_button_choice_diet(self):
        self.find(OPL.button_choice_diet).click()

    def click_random_popular_city(self):
        self.find_all(OPL.popular_cities)[random.randint(0, 19)].click()
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_all_elements_located(OPL.choice_menu))

    def menu_options(self):
        return self.find_all(OPL.text_menu)

    def number_step(self):
        return self.find_all(OPL.number_of_steps)

    def enter_city(self, city):
        self.find(OPL.enter_city).send_keys(city, Keys.ENTER)

    def choice_input_city(self, city):
        self.find(OPL.enter_city).send_keys(city)
        WebDriverWait(self.driver, 3).until(
            EC.invisibility_of_element(OPL.indicator_text))
        if self.find(OPL.text_empty_city).get_attribute('innerText') == 'Brak miasta o takiej nazwie':
            return self.find(OPL.text_empty_city).get_attribute('innerText')
        else:
            name_city = self.find(OPL.city_context).get_attribute('innerText')
            self.find(OPL.city_context).click()
            return name_city.split("\n")[0]

    def choice_diet_program(self, option):
        self.find_all(OPL.choice_menu)[option].click()

    def click_diet_standard(self):
        self.find_all(OPL.choice_diet)[0].click()

    def name_of_diets_selection(self):
        self.find_all(OPL.choice_diet)
        return self.find_all(OPL.choice_diet)

    def choice_diets_selection(self, option):
        self.find_all(OPL.choice_diet)[option].click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(OPL.all_calories))

    def all_standard_menu_diets(self):
        all_diets = list()
        all_elements = self.find_all(OPL.all_diets)
        for diet in all_elements:
            all_diets.append(diet.get_attribute('innerText'))
        return all_diets

    def all_calories(self):
        all_calories = list()
        all_elements = self.find_all(OPL.all_calories)
        for calorie in all_elements:
            all_calories.append(calorie.get_attribute('innerText'))
        return all_calories

    def choice_calories_or_click_calories_count(self, option):
        self.find_all(OPL.all_calories)[option].click()

    def calories_count(self, wiek, masa, wzrost, intensity, goal):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(OPL.indicator_text2))
        self.find(OPL.choice_sex_men).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(OPL.indicator_text2))
        self.find(OPL.field_age).click()
        self.find(OPL.field_age).send_keys(wiek)
        self.find(OPL.field_weight).click()
        self.find(OPL.field_weight).send_keys(masa)
        self.find(OPL.field_height).click()
        self.find(OPL.field_height).send_keys(wzrost)
        self.find(OPL.button_next2).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(OPL.indicator_text2))
        self.find_all(OPL.field_activity)[intensity].click()
        all_intensities = {0: 1.37, 1: 1.58, 2: 1.79, 3: 1.95}
        intensity = all_intensities[intensity]
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(OPL.indicator_text2))
        self.find_all(OPL.field_activity)[goal].click()
        self.find(OPL.button_accept_calories).click()
        sleep(3)
        all_goals = {0: -300, 1: 0, 2: 300}
        goal = all_goals[goal]
        cal = round((9.99 * masa + 6.242 * wzrost - 4.92 * wiek + 5) * intensity)
        result = int(self.find(OPL.numb_calories).get_attribute('innerText')[:-5])
        if abs(result * 0.5) <= abs(cal + goal) <= abs(result * 1.5):
            cal = result
            return cal

    def calorie_requirement(self):
        return int(self.find(OPL.numb_calories).get_attribute('innerText')[:-5])

    def number_all_diets_standard(self):
        all_diets = list()
        for diet in self.find_all(OPL.name_diets_standard):
            all_diets.append(diet.get_attribute('innerText'))
        return all_diets

    def choice_diet_in_standard_menu(self):
        self.find_all(OPL.diets_standard)[1].click()

    def click_description_diet_via_standard_menus(self, choice):
        self.find_all(OPL.description_diets)[choice].click()

    def name_description_diets(self):
        return self.find(OPL.name_description_diets).get_attribute('innerText')

    def day_on_page(self):
        day = self.find_all(OPL.day_today)[7].get_attribute('innerText')
        answer = {
            'poniedziałek': 'Monday',
            'wtorek': 'Tuesday',
            'środa': 'Wednesday',
            'czwartek': 'Thursday',
            'piątek': 'Friday',
            'sobota': 'Saturday',
            'niedziela': 'Sunday'
        }
        return answer[day]

    def day_real(self):
        date_now = datetime.datetime.now()
        return date_now.strftime('%A')

    def date_real(self):
        date_now = datetime.datetime.now()
        return date_now.strftime('%d.%m.%Y')

    def date_on_page(self):
        return self.find_all(OPL.date_today)[7].get_attribute('innerText')

    def click_button_meal_1(self):
        self.find_all(OPL.meal)[0].click()

    def click_button_meal_2(self):
        self.find_all(OPL.meal)[1].click()

    def click_button_meal_3(self):
        self.find_all(OPL.meal)[2].click()

    def message_that_a_smaller_number_cannot_be_selected(self):
        return self.find(OPL.message_via_minimal).get_attribute('innerText')

    def confirmation_of_minimum_order_message(self):
        self.find(OPL.button_accept_message_minimal_meals).click()

    def reporting_the_number_of_meals_selected(self):
        return self.find(OPL.message_number_of_meals_selected).get_attribute('innerText')

    def click_next_step(self):
        self.find(OPL.next_step).click()

    def output_order_detail_message(self):
        return self.find_all(OPL.order_detail_message)[0].get_attribute('innerText')

    def click_saturday_delivery_button(self):
        self.find(OPL.saturday_delivery_button).click()

    def click_sunday_delivery_button(self):
        self.find(OPL.sunday_delivery_button).click()

    def clickability_of_weekend_delivery_buttons(self):
        if self.find_all(OPL.blocked_weekends) == []:
            print(self.find_all(OPL.blocked_weekends))
            return False
        else:
            print(self.find_all(OPL.blocked_weekends))
            return True

    def active_day(self):
        return len(self.find_all(OPL.active_day))

    def ordering_days(self):
        return int(self.find(OPL.ordering_days).get_attribute('innerText'))

    def click_first_available_day(self):
        for day in self.find_all(OPL.calendar_days):
            day.click()
            if day.is_selected() is False:
                continue
            else:
                break
