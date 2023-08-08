from pages.order_page import OrderPage
import pytest


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
    assert order_page.number_step(-1) == 'Wybierz rodzaj programu'
    assert order_page.menu_options(0) == 'Program z Wyborem Menu'
    assert order_page.menu_options(1) == 'Program Standardowy'


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
    assert order_page.number_step(0) == 'Wybierz miasto'


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
    assert order_page.number_step(2) == 'Wybierz wariant'
    assert order_page.name_of_diets_selection(0) == 'STANDARD'
    assert order_page.name_of_diets_selection(1) == 'LADIES VIBES'


def test_correct_display_of_the_standard_menu(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    assert order_page.number_step(2) == 'Wybierz swoją dietę'
    assert order_page.all_standard_menu_diets() == [
        'Summer Vibes', 'Dieta Standard', 'Dieta ActivePro', 'Dieta Low IG', 'FODMAP', 'Gluten & Lactose Free',
        'Dieta Soft', 'Ketogeniczna', 'Wegetariańska i Ryby', 'Dieta Wegańska', 'Dieta Hashimoto', 'Detoks Sokowy',
        'Made by Chef', 'Ekonomiczna', 'Ekonomiczna Wege i Ryby', 'Dieta Progres'
    ]


def test_calorie_options_in_diets_when_selecting_menus_standard(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=0)
    order_page.choice_diets_selection(0)
    assert order_page.number_step(3) == 'Wybierz kaloryczność'
    assert order_page.all_calories() == ['1200', '1500', '1800', '2000', '2200', '2500', '3000', 'Dopasuj kaloryczność']


def test_calorie_options_in_diets_when_selecting_menus_ladies_vibes(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=0)
    order_page.choice_diets_selection(1)
    assert order_page.number_step(3) == 'Wybierz kaloryczność'
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
    assert diet == order_page.name_description_diets
    assert order_page.day_on_page() == order_page.day_real
    assert order_page.date_on_page() == order_page.date_real


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
    assert order_page.reporting_the_number_of_meals_selected == 'Ilość wybranych posiłków: 3 ok. 768kcal'


def test_moving_to_the_second_step_of_the_order(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    assert order_page.url_page == 'https://zamow.kuchniavikinga.pl/zamowienie/#/zamowienie'
    assert order_page.output_order_detail_message == 'Szczegóły zamówienia'


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


def test_correct_display_of_selected_days(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    assert order_page.selected_days == order_page.numbers_selected_days
    assert order_page.ordering_days == order_page.numbers_selected_days


def test_moving_to_the_third_step_of_the_order(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    order_page.click_button_next_step3()
    assert order_page.url_page == 'https://zamow.kuchniavikinga.pl/zamowienie/#/wybierz-dodatki'
    assert order_page.message_step3 == 'Wybierz dodatki'


def test_additive_addition(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    order_page.click_button_next_step3()
    order_page.click_additive_selection_button()
    order_page.click_additive_button()
    order_page.click_button_additive_next()
    assert order_page.message_amount_of_additives == '1'


def test_moving_to_the_fourth_step_of_the_order(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    selected_days = order_page.numbers_selected_days
    order_page.click_button_next_step3()
    order_page.click_additive_selection_button()
    order_page.click_additive_button()
    order_page.click_button_additive_next()
    order_page.click_button_next_step4()
    assert order_page.url_page == 'https://zamow.kuchniavikinga.pl/zamowienie/#/koszyk'
    assert order_page.message_step4_ordering_days == selected_days
    assert 'Suma dodatków' in order_page.order_confirmation_message_for_supplements
    assert 'Dieta Standard' in order_page.order_confirmation_diet_message


def test_moving_to_the_fifth_step_of_the_order(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    order_page.click_button_next_step3()
    order_page.click_additive_selection_button()
    order_page.click_additive_button()
    order_page.click_button_additive_next()
    order_page.click_button_next_step4()
    order_page.click_button_next_step5()
    assert order_page.url_page == 'https://zamow.kuchniavikinga.pl/zamowienie/#/platnosc'


def test_transfer_to_the_contact_page_for_ordering(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    order_page.click_button_next_step3()
    order_page.click_additive_selection_button()
    order_page.click_additive_button()
    order_page.click_button_additive_next()
    order_page.click_button_next_step4()
    order_page.click_button_next_step5()
    order_page.click_continue_button_without_registration()
    order_page.click_confirmation_button_to_continue_as_a_guest()
    assert order_page.url_page == 'https://zamow.kuchniavikinga.pl/zamowienie/#/platnosc'


@pytest.mark.parametrize(
    "first_name",
    ['',
     ' sdmfhsdf sdmnfbsndf',
     '2',
     '!#@%$&^!%#$&^@Hjhfdgfjhsd  sjdgfjhsdgf JHSAGDJHASGD13123 4hgsdfngKASDJSFJDANSKDJNASDKJ',
     '                                             2',
     'фыввапвапdf,mgndfgm,@#@#   a,sdm',
     'K',
     '#']
)
def test_enter_first_name(driver, first_name):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    order_page.click_button_next_step3()
    order_page.click_additive_selection_button()
    order_page.click_additive_button()
    order_page.click_button_additive_next()
    order_page.click_button_next_step4()
    order_page.click_button_next_step5()
    order_page.click_continue_button_without_registration()
    order_page.click_confirmation_button_to_continue_as_a_guest()
    order_page.enter_first_name(first_name)
    order_page.click_privacy_policy_consent()
    order_page.click_pay_button()
    assert order_page.message_first_name_error(first_name) is True


@pytest.mark.parametrize(
    "second_name",
    ['',
     ' sdmfhsdf sdmnfbsndf',
     '2',
     '!#@%$&^!%#$&^@Hjhfdgfjhsd  sjdgfjhsdgf JHSAGDJHASGD13123 4hgsdfngKASDJSFJDANSKDJNASDKJ',
     '                                             2',
     'фыввапвапdf,mgndfgm,@#@#   a,sdm',
     'K',
     '#']
)
def test_enter_second_name(driver, second_name):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    order_page.click_button_next_step3()
    order_page.click_additive_selection_button()
    order_page.click_additive_button()
    order_page.click_button_additive_next()
    order_page.click_button_next_step4()
    order_page.click_button_next_step5()
    order_page.click_continue_button_without_registration()
    order_page.click_confirmation_button_to_continue_as_a_guest()
    order_page.enter_second_name(second_name)
    order_page.click_privacy_policy_consent()
    order_page.click_pay_button()
    assert order_page.message_second_name_error(second_name) is True


@pytest.mark.parametrize(
    "email",
    ['',
     'asd@asd.a',
     'a@a.a',
     ' asasd@asd.com',
     'asd@asdf',
     'asd.asdf',
     '!@#!#$@#$@#@.asdsad123.asd',
     '@A.SD@asd',
     'asdasdas@asd.asd@',
     'asd..asd@asd.asd',
     'asd@asd.asd.',
     '.asd@asd.asd',
     'asd.@asd.asd',
     'asd@.asd.asd',
     'asd@a#@#@#@$%*(&^%*&^%sd.asd']
)
def test_enter_email(driver, email):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    order_page.click_button_next_step3()
    order_page.click_additive_selection_button()
    order_page.click_additive_button()
    order_page.click_button_additive_next()
    order_page.click_button_next_step4()
    order_page.click_button_next_step5()
    order_page.click_continue_button_without_registration()
    order_page.click_confirmation_button_to_continue_as_a_guest()
    order_page.enter_email(email)
    order_page.click_privacy_policy_consent()
    order_page.click_pay_button()
    assert order_page.message_email_error(email) is True


@pytest.mark.parametrize(
    "phone_number",
    ['',
     '1',
     '12',
     '123',
     '1234',
     '12345',
     '123456',
     '1234567',
     '12345678',
     '123456789',
     '1234567890',
     '12345678901',
     '123456789012']
)
def test_enter_phone_number(driver, phone_number):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    order_page.click_button_next_step3()
    order_page.click_additive_selection_button()
    order_page.click_additive_button()
    order_page.click_button_additive_next()
    order_page.click_button_next_step4()
    order_page.click_button_next_step5()
    order_page.click_continue_button_without_registration()
    order_page.click_confirmation_button_to_continue_as_a_guest()
    order_page.enter_phone_number(phone_number)
    order_page.click_privacy_policy_consent()
    order_page.click_pay_button()
    assert order_page.message_phone_number_error(phone_number) is True


def test_enter_empty_index(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    order_page.click_button_next_step3()
    order_page.click_additive_selection_button()
    order_page.click_additive_button()
    order_page.click_button_additive_next()
    order_page.click_button_next_step4()
    order_page.click_button_next_step5()
    order_page.click_continue_button_without_registration()
    order_page.click_confirmation_button_to_continue_as_a_guest()
    order_page.click_privacy_policy_consent()
    order_page.click_pay_button()
    assert order_page.message_index_error() is True


def test_enter_index(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    order_page.click_button_next_step3()
    order_page.click_additive_selection_button()
    order_page.click_additive_button()
    order_page.click_button_additive_next()
    order_page.click_button_next_step4()
    order_page.click_button_next_step5()
    order_page.click_continue_button_without_registration()
    order_page.click_confirmation_button_to_continue_as_a_guest()
    order_page.click_field_index_and_enter_value_and_select_index('0')
    order_page.click_privacy_policy_consent()
    order_page.click_pay_button()
    assert order_page.message_index_error() is False


@pytest.mark.parametrize(
    "street",
    ['',
     ' sdmfhsdf sdmnfbsndf',
     '2',
     '!#@%$&^!%#$&^@Hjhfdgfjhsd  sjdgfjhsdgf JHSAGDJHASGD13123 4hgsdfngKASDJSFJDANSKDJNASDKJ',
     '                                             2',
     'фыввапвапdf,mgndfgm,@#@#   a,sdm',
     'K',
     '#']
)
def test_enter_street(driver, street):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    order_page.click_button_next_step3()
    order_page.click_additive_selection_button()
    order_page.click_additive_button()
    order_page.click_button_additive_next()
    order_page.click_button_next_step4()
    order_page.click_button_next_step5()
    order_page.click_continue_button_without_registration()
    order_page.click_confirmation_button_to_continue_as_a_guest()
    order_page.enter_street(street)
    order_page.click_privacy_policy_consent()
    order_page.click_pay_button()
    assert order_page.message_street_error(street) is True


@pytest.mark.parametrize(
    "house_number",
    ['',
     ' sdmfhsdf sdmnfbsndf',
     '2',
     '!#@%$&^!%#$&^@Hjhfdgfjhsd  sjdgfjhsdgf JHSAGDJHASGD13123 4hgsdfngKASDJSFJDANSKDJNASDKJ',
     '                                             2',
     'фыввапвапdf,mgndfgm,@#@#   a,sdm',
     'K',
     '#']
)
def test_enter_house_number(driver, house_number):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    order_page.click_button_next_step3()
    order_page.click_additive_selection_button()
    order_page.click_additive_button()
    order_page.click_button_additive_next()
    order_page.click_button_next_step4()
    order_page.click_button_next_step5()
    order_page.click_continue_button_without_registration()
    order_page.click_confirmation_button_to_continue_as_a_guest()
    order_page.enter_house_number(house_number)
    order_page.click_privacy_policy_consent()
    order_page.click_pay_button()
    assert order_page.message_house_number_error(house_number) is True


@pytest.mark.parametrize(
    "floor_number",
    ['',
     '1',
     '12',
     '123',
     '1234',
     '12345',
     '123456',
     '1234567',
     '12345678',
     '123456789',
     '1234567890',
     '12345678901',
     '123456789012']
)
def test_enter_floor_number(driver, floor_number):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    order_page.click_button_next_step3()
    order_page.click_additive_selection_button()
    order_page.click_additive_button()
    order_page.click_button_additive_next()
    order_page.click_button_next_step4()
    order_page.click_button_next_step5()
    order_page.click_continue_button_without_registration()
    order_page.click_confirmation_button_to_continue_as_a_guest()
    order_page.enter_floor_number(floor_number)
    order_page.click_privacy_policy_consent()
    order_page.click_pay_button()
    assert order_page.message_floor_number_error(floor_number) is True


@pytest.mark.parametrize(
    "stairwell_number",
    ['',
     '1',
     '12',
     '123',
     '1234',
     '12345',
     '123456',
     '1234567',
     '12345678',
     '123456789',
     '1234567890',
     '12345678901',
     '123456789012']
)
def test_enter_stairwell_number(driver, stairwell_number):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    order_page.click_button_next_step3()
    order_page.click_additive_selection_button()
    order_page.click_additive_button()
    order_page.click_button_additive_next()
    order_page.click_button_next_step4()
    order_page.click_button_next_step5()
    order_page.click_continue_button_without_registration()
    order_page.click_confirmation_button_to_continue_as_a_guest()
    order_page.enter_stairwell_number(stairwell_number)
    order_page.click_privacy_policy_consent()
    order_page.click_pay_button()
    assert order_page.message_stairwell_number_error(stairwell_number) is True


def test_enter_empty_delivery_time(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    order_page.click_button_next_step3()
    order_page.click_additive_selection_button()
    order_page.click_additive_button()
    order_page.click_button_additive_next()
    order_page.click_button_next_step4()
    order_page.click_button_next_step5()
    order_page.click_continue_button_without_registration()
    order_page.click_confirmation_button_to_continue_as_a_guest()
    order_page.click_privacy_policy_consent()
    order_page.click_pay_button()
    assert order_page.message_delivery_time_error() is True


def test_enter_delivery_time(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    order_page.click_button_next_step3()
    order_page.click_additive_selection_button()
    order_page.click_additive_button()
    order_page.click_button_additive_next()
    order_page.click_button_next_step4()
    order_page.click_button_next_step5()
    order_page.click_continue_button_without_registration()
    order_page.click_confirmation_button_to_continue_as_a_guest()
    order_page.select_delivery_time()
    order_page.click_privacy_policy_consent()
    order_page.click_pay_button()
    assert order_page.message_delivery_time_error() is False


def test_navigation_to_the_payment_page(driver):
    order_page = OrderPage(driver)
    order_page.open_page()
    order_page.click_random_popular_city()
    order_page.choice_diet_program(option=1)
    order_page.choice_diet_in_standard_menu()
    order_page.choice_calories_or_click_calories_count(0)
    order_page.click_next_step()
    order_page.click_first_available_day()
    order_page.click_button_next_step3()
    order_page.click_additive_selection_button()
    order_page.click_additive_button()
    order_page.click_button_additive_next()
    order_page.click_button_next_step4()
    order_page.click_button_next_step5()
    order_page.click_continue_button_without_registration()
    order_page.click_confirmation_button_to_continue_as_a_guest()
    order_page.enter_first_name('Blablabla')
    order_page.enter_second_name('Blablabla')
    order_page.enter_email('asd@asd.asd')
    order_page.enter_phone_number('123456789')
    order_page.click_field_index_and_enter_value_and_select_index('0')
    order_page.enter_street('blablabla')
    order_page.enter_house_number('blablabla')
    order_page.enter_floor_number('123')
    order_page.enter_stairwell_number('12345')
    order_page.select_delivery_time()
    order_page.click_privacy_policy_consent()
    order_page.click_pay_button()
    assert 'https://secure.tpay.com/' in order_page.url_page_finish
