from pages.order_page import OrderPage
import pytest
import random
from time import sleep


def test_choice_step_diet_without_order(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_step_button_choice_diet()
    assert order_page.url_page == 'https://zamow.kuchniavikinga.pl/zamowienie/#/'


def test_choice_step_date_without_order(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_step_button_choice_date()
    assert order_page.url_page == 'https://zamow.kuchniavikinga.pl/zamowienie/#/'


def test_choice_step_add_without_order(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_step_button_choice_add()
    assert order_page.url_page == 'https://zamow.kuchniavikinga.pl/zamowienie/#/'


def test_choice_step_cart_without_order(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_step_button_choice_cart()
    assert order_page.url_page == 'https://zamow.kuchniavikinga.pl/zamowienie/#/koszyk'


def test_choice_step_cart_and_refund_without_order(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_step_button_choice_cart()
    order_page.click_button_choice_diet()
    assert order_page.url_page == 'https://zamow.kuchniavikinga.pl/zamowienie/#/'


def test_choice_step_data_without_order(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_step_button_choice_data()
    assert order_page.url_page == 'https://zamow.kuchniavikinga.pl/zamowienie/#/'


def test_correct_choice_city(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    assert order_page.number_step()[-1].get_attribute('innerText') == 'Wybierz rodzaj programu'
    assert order_page.menu_options()[0].get_attribute('innerText') == 'Program z Wyborem Menu'
    assert order_page.menu_options()[1].get_attribute('innerText') == 'Program Standardowy'


@pytest.mark.parametrize(
    "city",
    ['Ciechocinek',
     'Piła',
     'Oława']
)
def test_correct_input_city_and_choice_via_button_enter(driver, city):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.enter_city(city)
    assert order_page.number_step()[0].get_attribute('innerText') == 'Wybierz miasto'


@pytest.mark.parametrize(
    "city",
    ['Ciechoci',
     'Pił',
     'Oław']
)
def test_correct_search_city_by_part_name(driver, city):
    order_page = OrderPage(driver)
    order_page.open_page()
    name_city = order_page.choice_input_city(city)
    assert name_city in ['Ciechocinek', 'Piła', 'Oława']


@pytest.mark.parametrize(
    "city",
    ['   Ciechoci',
     'Pił     ',
     '     ołAw     ']
)
def test_correct_search_city_by_part_name_with_space_and_different_case(driver, city):
    order_page = OrderPage(driver)
    order_page.open_page()
    name_city = order_page.choice_input_city(city)
    assert name_city in ['Ciechocinek', 'Piła', 'Oława']


@pytest.mark.parametrize(
    "city",
    ['CCiechoci',
     'Piłtqweqwe     ',
     '    asd ołAw asdasd    ']
)
def test_correct_search_city_by_part_name_with_space_and_different_case(driver, city):
    order_page = OrderPage(driver)
    order_page.open_page()
    notification = order_page.choice_input_city(city)
    assert notification == 'Brak miasta o takiej nazwie'


def test_correct_display_of_the_selection_menu(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=0)
    assert order_page.number_step()[2].get_attribute('innerText') == 'Wybierz wariant'
    assert order_page.name_of_diets_selection()[0].get_attribute('innerText').split("\n")[0] == 'STANDARD'
    assert order_page.name_of_diets_selection()[1].get_attribute('innerText').split("\n")[0] == 'LADIES VIBES'


def test_correct_display_of_the_standard_menu(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    assert order_page.number_step()[2].get_attribute('innerText') == 'Wybierz swoją dietę'
    assert order_page.all_standard_menu_diets() == [
        'Summer Vibes', 'Dieta Standard', 'Dieta ActivePro', 'Dieta Low IG', 'FODMAP', 'Gluten & Lactose Free',
        'Dieta Soft', 'Ketogeniczna', 'Wegetariańska i Ryby', 'Dieta Wegańska', 'Dieta Hashimoto', 'Detoks Sokowy',
        'Made by Chef', 'Ekonomiczna', 'Ekonomiczna Wege i Ryby', 'Dieta Progres'
    ]


def test_calorie_options_in_diets_when_selecting_menus(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=0)
    order_page.choice_diets_selection(0)
    assert order_page.number_step()[3].get_attribute('innerText') == 'Wybierz kaloryczność'
    assert order_page.all_calories() == ['1200', '1500', '1800', '2000', '2200', '2500', '3000', 'Dopasuj kaloryczność']
    order_page.choice_diets_selection(1)
    assert order_page.number_step()[3].get_attribute('innerText') == 'Wybierz kaloryczność'
    assert order_page.all_calories() == ['1200', '1500', '1800', '2000', 'Dopasuj kaloryczność']


@pytest.mark.parametrize(
    "wiek,masa,wzrost,intensity,goal",
    [(30, 90, 188, 0, 1),
     (25, 923, 188, 1, 1),
     (45, 910, 345, 2, 1),
     (15, 1, 112, 3, 1),
     (2, 90, 786, 3, 1),
     (10, 90, 345, 1, 0),
     (99, 90, 96, 1, 1),
     (1, 2, 56, 1, 2),
     (23, 90, 2, 0, 0),
     (30, 3, 9, 3, 2)]
)
def test_correct_calorie_count(driver, wiek, masa, wzrost, intensity, goal):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=0)
    order_page.choice_diets_selection(0)
    order_page.choice_calories_or_click_calories_count(-1)
    expected = order_page.calories_count(wiek, masa, wzrost, intensity, goal)
    actual = order_page.calorie_requirement()
    assert expected == actual


def test_correct_description_of_the_diet_when_standard_menus(driver, choice=1):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    all_diets = order_page.number_all_diets_standard()
    diet = all_diets[choice]
    order_page.click_description_diet_via_standard_menus(choice)
    assert all_diets == ['Summer Vibes', 'Dieta Standard', 'Dieta ActivePro',
                         'Dieta Low IG', 'FODMAP', 'Gluten & Lactose Free',
                         'Dieta Soft', 'Ketogeniczna', 'Wegetariańska i Ryby',
                         'Dieta Wegańska', 'Dieta Hashimoto', 'Detoks Sokowy',
                         'Made by Chef', 'Ekonomiczna', 'Ekonomiczna Wege i Ryby',
                         'Dieta Progres']
    assert diet == order_page.name_description_diets()
    assert order_page.day_on_page() == order_page.day_real()
    assert order_page.date_on_page() == order_page.date_real()


def test_minimum_number_of_meals_on_a_standard_menu(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_button_meal_1()
    order_page.click_button_meal_2()
    order_page.click_button_meal_3()
    message_via_minimal = order_page.message_that_a_smaller_number_cannot_be_selected()
    order_page.confirmation_of_minimum_order_message()
    assert message_via_minimal == 'Osiągnięto maksymalną ilość dodatków.'
    assert order_page.reporting_the_number_of_meals_selected() == 'Ilość wybranych posiłków: 3 ok. 768kcal'


def test_moving_to_the_second_step_of_the_order(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    assert order_page.url_page == 'https://zamow.kuchniavikinga.pl/zamowienie/#/zamowienie'
    assert order_page.output_order_detail_message() == 'Szczegóły zamówienia'


def test_weekend_delivery_ban(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    result_before = order_page.clickability_of_weekend_delivery_buttons()
    order_page.click_saturday_delivery_button()
    order_page.click_sunday_delivery_button()
    result_after = order_page.clickability_of_weekend_delivery_buttons()
    assert result_before != result_after


def test_wesdekend_delivery_ban(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    assert order_page.active_day() == order_page.ordering_days()


