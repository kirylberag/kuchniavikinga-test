from pages.base_page import BasePage
from locators import order_page_locators as OPL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import datetime
import random
import allure


@allure.feature('Order page')
class OrderPage(BasePage):
    page_url = '/zamowienie/'
    beginning_url = '//zamow.'

    @property
    @allure.step('Display page title')
    def page_title(self):
        return self.driver.title

    @property
    @allure.step('Display url page')
    def url_page(self):
        return self.driver.current_url

    @allure.step('click step button choice diet')
    def click_step_button_choice_diet(self):
        self.find_all(OPL.step_order)[0].click()

    @allure.step('click step button choice date')
    def click_step_button_choice_date(self):
        self.find_all(OPL.step_order)[1].click()

    @allure.step('click step button choice add')
    def click_step_button_choice_add(self):
        self.find_all(OPL.step_order)[2].click()

    @allure.step('click step button choice cart')
    def click_step_button_choice_cart(self):
        self.find_all(OPL.step_order)[3].click()

    @allure.step('click step button choice data')
    def click_step_button_choice_data(self):
        self.find_all(OPL.step_order)[4].click()

    @allure.step('click button choice diet')
    def click_button_choice_diet(self):
        self.find(OPL.button_choice_diet).click()

    @allure.step('Selecting a random suggested city')
    def click_random_popular_city(self):
        self.find_all(OPL.popular_cities)[random.randint(0, 19)].click()
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_all_elements_located(OPL.choice_menu))

    @allure.step('Menu selection 0 - first, 1 - second')
    def menu_options(self, option):
        return self.find_all(OPL.text_menu)[option].get_attribute('innerText')

    @allure.step('number step')
    def number_step(self, option):
        return self.find_all(OPL.number_of_steps)[option].get_attribute('innerText')

    @allure.step('Enter city')
    def enter_city(self, city):
        self.find(OPL.enter_city).send_keys(city, Keys.ENTER)

    @allure.step('Choice input city')
    def choice_input_city(self, city):
        self.find(OPL.enter_city).send_keys(city)
        WebDriverWait(self.driver, 3).until(
            EC.invisibility_of_element(OPL.indicator_text))
        try:
            return self.find(OPL.text_empty_city).get_attribute('innerText')
        except:
            name_city = self.find(OPL.city_context).get_attribute('innerText')
            self.find(OPL.city_context).click()
            return name_city.split("\n")[0]

    @allure.step('Choice diet program')
    def choice_diet_program(self, option):
        self.find_all(OPL.choice_menu)[option].click()

    @allure.step('Choice diet standard')
    def click_diet_standard(self):
        self.find_all(OPL.choice_diet)[0].click()

    @allure.step('name of diets selection')
    def name_of_diets_selection(self, option):
        self.find_all(OPL.choice_diet)
        return self.find_all(OPL.choice_diet)[option].get_attribute('innerText').split("\n")[0]

    @allure.step('Choice diets selection')
    def choice_diets_selection(self, option):
        self.find_all(OPL.choice_diet)[option].click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(OPL.all_calories))

    @allure.step('All standard menu diets')
    def all_standard_menu_diets(self):
        all_diets = list()
        all_elements = self.find_all(OPL.all_diets)
        for diet in all_elements:
            all_diets.append(diet.get_attribute('innerText'))
        return all_diets

    @allure.step('All calories')
    def all_calories(self):
        all_calories = list()
        all_elements = self.find_all(OPL.all_calories)
        for calorie in all_elements:
            all_calories.append(calorie.get_attribute('innerText'))
        return all_calories

    @allure.step('Choice calories or click calories count [-1] - count')
    def choice_calories_or_click_calories_count(self, option):
        self.find_all(OPL.all_calories)[option].click()

    @allure.step('calories count')
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
        all_goals = {0: -300, 1: 0, 2: 300}
        goal = all_goals[goal]
        cal = round((9.99 * masa + 6.242 * wzrost - 4.92 * wiek + 5) * intensity)
        result = int(self.find(OPL.numb_calories).get_attribute('innerText')[:-5])
        if abs(result * 0.5) <= abs(cal + goal) <= abs(result * 1.5):
            cal = result
            return cal

    @allure.step('calorie_requirement')
    def calorie_requirement(self):
        return int(self.find(OPL.numb_calories).get_attribute('innerText')[:-5])

    @allure.step('number_all_diets_standard')
    def number_all_diets_standard(self):
        all_diets = list()
        for diet in self.find_all(OPL.name_diets_standard):
            all_diets.append(diet.get_attribute('innerText'))
        return all_diets

    @allure.step('choice_diet_in_standard_menu')
    def choice_diet_in_standard_menu(self):
        self.find_all(OPL.diets_standard)[1].click()

    @allure.step('click_description_diet_via_standard_menus')
    def click_description_diet_via_standard_menus(self, choice):
        self.find_all(OPL.description_diets)[choice].click()

    @property
    @allure.step('name_description_diets')
    def name_description_diets(self):
        return self.find(OPL.name_description_diets).get_attribute('innerText')

    @allure.step('day_on_page')
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

    @property
    @allure.step('day_real')
    def day_real(self):
        date_now = datetime.datetime.now()
        return date_now.strftime('%A')

    @property
    @allure.step('date_real')
    def date_real(self):
        date_now = datetime.datetime.now()
        result = date_now.strftime('%d.%m.%Y')
        if result[0] == '0':
            return result[1:]
        else:
            return result

    @allure.step('date_on_page')
    def date_on_page(self):
        return self.find_all(OPL.date_today)[7].get_attribute('innerText')

    @allure.step('click_button_meal_1')
    def click_button_meal_1(self):
        self.find_all(OPL.meal)[0].click()

    @allure.step('click_button_meal_2')
    def click_button_meal_2(self):
        self.find_all(OPL.meal)[1].click()

    @allure.step('click_button_meal_3')
    def click_button_meal_3(self):
        self.find_all(OPL.meal)[2].click()

    @allure.step('message_that_a_smaller_number_cannot_be_selected')
    def message_that_a_smaller_number_cannot_be_selected(self):
        return self.find(OPL.message_via_minimal).get_attribute('innerText')

    @allure.step('confirmation_of_minimum_order_message')
    def confirmation_of_minimum_order_message(self):
        self.find(OPL.button_accept_message_minimal_meals).click()


    @property
    @allure.step('reporting_the_number_of_meals_selected')
    def reporting_the_number_of_meals_selected(self):
        return self.find(OPL.message_number_of_meals_selected).get_attribute('innerText')

    @allure.step('click_next_step')
    def click_next_step(self):
        self.find(OPL.next_step).click()

    @property
    @allure.step('output_order_detail_message')
    def output_order_detail_message(self):
        return self.find_all(OPL.order_detail_message)[0].get_attribute('innerText')

    @allure.step('click_saturday_delivery_button')
    def click_saturday_delivery_button(self):
        self.find(OPL.saturday_delivery_button).click()

    @allure.step('click_sunday_delivery_button')
    def click_sunday_delivery_button(self):
        self.find(OPL.sunday_delivery_button).click()

    @allure.step('clickability_of_weekend_delivery_buttons')
    def clickability_of_weekend_delivery_buttons(self):
        if not self.find_all(OPL.blocked_weekends):
            return False
        else:
            return True

    @property
    @allure.step('selected_days')
    def selected_days(self):
        return len(self.find_all(OPL.selected_days))

    @property
    @allure.step('ordering_days')
    def ordering_days(self):
        return int(self.find_all(OPL.numbers_days)[2].get_attribute('innerText'))

    @allure.step('click_first_available_day')
    def click_first_available_day(self):
        self.find_all(OPL.active_days)[0].click()

    @allure.step('click_button_next_step3')
    def click_button_next_step3(self):
        self.find_all(OPL.button_next3)[2].click()

    @property
    @allure.step('message_step3')
    def message_step3(self):
        return self.find_all(OPL.text_step3)[0].get_attribute('innerText')

    @allure.step('click_additive_selection_button')
    def click_additive_selection_button(self):
        self.find_all(OPL.additive_selection_button)[0].click()

    @allure.step('click_additive_button')
    def click_additive_button(self):
        self.find_all(OPL.additive_button)[3].click()

    @allure.step('click_button_additive_next')
    def click_button_additive_next(self):
        self.find(OPL.button_additive_next).click()

    @property
    @allure.step('message_amount_of_additives')
    def message_amount_of_additives(self):
        return self.find_all(OPL.amount_of_additives)[1].get_attribute('innerText')

    @allure.step('click_button_next_step4')
    def click_button_next_step4(self):
        self.find(OPL.button_next4).click()

    @property
    @allure.step('message_step4_ordering_days')
    def message_step4_ordering_days(self):
        return int(self.find(OPL.step4_ordering_days).get_attribute('innerText')[:-3])

    @property
    @allure.step('numbers_selected_days')
    def numbers_selected_days(self):
        return int(self.find(OPL.numbers_selected_days).get_attribute('value'))

    @property
    @allure.step('order_confirmation_message_for_supplements')
    def order_confirmation_message_for_supplements(self):
        return self.find(OPL.message_for_supplements).get_attribute('innerText')

    @property
    @allure.step('order_confirmation_diet_message')
    def order_confirmation_diet_message(self):
        return self.find(OPL.diet_message).get_attribute('innerText')

    @allure.step('click_button_next_step5')
    def click_button_next_step5(self):
        self.find(OPL.button_next5).click()

    @allure.step('click_confirmation_button_to_continue_as_a_guest')
    def click_confirmation_button_to_continue_as_a_guest(self):
        self.find(OPL.confirmation_button_to_continue_as_a_guest).click()

    @allure.step('click_continue_button_without_registration')
    def click_continue_button_without_registration(self):
        self.find_all(OPL.continue_button_without_registration)[1].click()

    @allure.step('enter_first_name')
    def enter_first_name(self, first_name):
        self.find(OPL.first_name).send_keys(first_name)

    @allure.step('enter_second_name')
    def enter_second_name(self, second_name):
        self.find(OPL.second_name).send_keys(second_name)

    @allure.step('enter_email')
    def enter_email(self, email):
        self.find(OPL.email).send_keys(email)

    @allure.step('enter_phone_number')
    def enter_phone_number(self, phone_number):
        self.find(OPL.phone_number).send_keys(phone_number)

    @allure.step('click_field_index_and_enter_value_and_select_index')
    def click_field_index_and_enter_value_and_select_index(self, index):
        self.find(OPL.field_index).send_keys(index)
        WebDriverWait(self.driver, 3).until(
            EC.invisibility_of_element(OPL.indicator_text))
        self.find(OPL.select_index).click()

    @allure.step('enter_street')
    def enter_street(self, street):
        self.find(OPL.street).send_keys(street)

    @allure.step('enter_house_number')
    def enter_house_number(self, house_number):
        self.find(OPL.house_number).send_keys(house_number)

    @allure.step('enter_floor_number')
    def enter_floor_number(self, floor_number):
        self.find(OPL.floor_number).send_keys(floor_number)

    @allure.step('enter_stairwell_number')
    def enter_stairwell_number(self, stairwell_number):
        self.find(OPL.stairwell_number).send_keys(stairwell_number)

    @allure.step('select_delivery_time')
    def select_delivery_time(self):
        self.find(OPL.field_delivery_time).click()
        self.find(OPL.select_delivery_time).click()

    @allure.step('click_privacy_policy_consent')
    def click_privacy_policy_consent(self):
        self.find(OPL.privacy_policy_consent).click()

    @allure.step('click_pay_button')
    def click_pay_button(self):
        self.find(OPL.pay_button).click()

    @allure.step('message_index_error')
    def message_index_error(self):
        try:
            return self.find(OPL.index_error).get_attribute('innerText') == 'Kod pocztowy jest wymagany'
        except:
            return False

    @allure.step('cmessage_delivery_time_error')
    def message_delivery_time_error(self):
        try:
            return self.find(OPL.delivery_time_error).get_attribute('innerText') == 'Godzina dostawy jest wymagana'
        except:
            return False

    @allure.step('message_first_name_error')
    def message_first_name_error(self, first_name):
        if first_name == '':
            return self.find(OPL.first_name_error).get_attribute('innerText') == 'Imię jest wymagane'
        else:
            return True

    @allure.step('message_second_name_error')
    def message_second_name_error(self, second_name):
        if second_name == '':
            return self.find(OPL.second_name_error).get_attribute('innerText') == 'Nazwisko jest wymagane'
        else:
            return True

    @allure.step('message_email_error')
    def message_email_error(self, email):
        if '@' in email:
            number_index = email.index('@')
            validation = email[number_index:]
        if email == '':
            return self.find(OPL.email_error).get_attribute('innerText') == 'Email jest wymagany'
        elif ' ' in email:
            return self.find(OPL.email_error3).get_attribute('innerText') == 'Adres email nie może zawierać spacji'
        elif (
            '@' not in email
            or '.' not in email
            or (email.count('@') > 1)
            or (email[-1] == '@')
            or (email[0] == '@')
            or ('..' in email)
            or (email[-1] == '.')
            or (email[0] == '.')
            or ('@.' in email)
            or ('.@' in email)
            or ('.' not in validation)
            or (any(char in ",:;!_*-+()/#¤%&)'~!#$%^&*()_+{}|:”>?<!”№;:?*()/,;’[]" for char in validation))
        ):
            return self.find(OPL.email_error2).get_attribute('innerText') == 'Wpisz poprawny adres email'
        else:
            return True

    @allure.step('message_phone_number_error')
    def message_phone_number_error(self, phone_number):
        if phone_number == '':
            return self.find(OPL.phone_number_error).get_attribute('innerText') == 'Telefon jest wymagany'
        elif 0 < len(phone_number) < 7 or len(phone_number) == 8 or 9 < len(phone_number) < 13:
            return self.find(OPL.phone_number_error2).get_attribute('innerText') == (
                'Wprowadź poprawny numer (np. 123456789)')
        else:
            return True

    @allure.step('message_street_error')
    def message_street_error(self, street):
        if street == '':
            return self.find(OPL.street_error).get_attribute('innerText') == 'Ulica jest wymagana'
        else:
            return True

    @allure.step('message_house_number_error')
    def message_house_number_error(self, house_number):
        if house_number == '':
            return self.find(OPL.house_number_error).get_attribute('innerText') == 'Numer domu jest wymagany'
        else:
            return True

    @allure.step('message_floor_number_error')
    def message_floor_number_error(self, floor_number):
        if len(floor_number) > 10:
            return self.find(OPL.floor_number_error).get_attribute('innerText') == 'Numer piętra jest za długi'
        else:
            return True

    @allure.step('message_stairwell_number_error')
    def message_stairwell_number_error(self, stairwell_number):
        if len(stairwell_number) > 10:
            return self.find(OPL.stairwell_number_error).get_attribute('innerText') == 'Numer klatki jest za długi'
        else:
            return True

    @property
    @allure.step('url_page_finish')
    def url_page_finish(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(OPL.finish_indicator))
        return self.driver.current_url
