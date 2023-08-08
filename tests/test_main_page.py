from pages.main_page import MainPage
from pages.calorie_count_result_page import CalorieResultPage
from pages.order_page import OrderPage
from pages.other_page import OtherPage
import pytest
import allure


@pytest.mark.parametrize(
    "sex,wzrost,masa,wiek,intensity,goal",
    [(1, 188, 90, 30, 1.4, 1),
     (1, 200, 90, 30, 1.5, 2),
     (1, 175, 80, 25, 1.7, 3),
     (1, 188, 70, 40, 1.9, 1),
     (1, 190, 90, 30, 2.2, 1),
     (2, 180, 60, 45, 1.4, 1),
     (2, 188, 70, 34, 1.5, 2),
     (2, 175, 65, 23, 1.7, 3),
     (2, 168, 53, 64, 1.9, 1),
     (2, 190, 60, 99, 2.2, 1),
     (1, 190, 70, 99, None, 1),
     (2, 175, 80, 99, 2.2, None),
     (1, 180, 100, 99, None, None)]
)
@allure.story('calories_counting_with_valid_values')
def test_calories_counting_with_valid_values(driver, sex, wzrost, masa, wiek, intensity, goal):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.calorie_counting(sex, wzrost, masa, wiek, intensity, goal)
    result_page = CalorieResultPage(driver)
    assert result_page.reporting_calories_needed[0] == (
        result_page.calorie_count_check(wzrost, masa, wiek, intensity, goal)
    )


@pytest.mark.parametrize(
    "sex,wzrost,masa,wiek,intensity,goal",
    [(1, '188asd', 90, 30, 1.4, 1),
     (1, 'asd188', 90, 30, 1.4, 1),
     (1, '23a#d188', 90, 30, 1.4, 1),
     (2, '#@%35$', 90, 30, 1.4, 1),
     (1, 200, 'asd90', 30, 1.5, 2),
     (2, 200, ' ', 30, 1.5, 2),
     (1, -200, 'asd', -30, 1.5, 2),
     (1, 175, 80, '25asd$%^', 1.7, 3),
     (1, 0, 0, 0, 1.4, 2),
     (2, 0, 999999999, 0, 2.2, 3)]
)
@allure.story('calories_counting_with_invalid_values')
def test_calories_counting_with_invalid_values(driver, sex, wzrost, masa, wiek, intensity, goal):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.calorie_counting(sex, wzrost, masa, wiek, intensity, goal)
    result_page = CalorieResultPage(driver)
    assert result_page.reporting_calories_needed[0] == (
        result_page.calorie_count_check(wzrost, masa, wiek, intensity, goal)
    )


@allure.story('stop_sliding_with_cursor_lock')
def test_stop_sliding_with_cursor_lock(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    initial_list_boxes = main_page.visible_list_boxes()
    list_boxes_after_fixing_the_cursor = main_page.identical_visible_boxes_after_fixed_the_cursor()
    assert initial_list_boxes == list_boxes_after_fixing_the_cursor


@allure.story('carousel_sliding_without_fixation')
def test_carousel_sliding_without_fixation(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    initial_list_boxes = main_page.visible_list_boxes()
    list_boxes_without_fixing_the_cursor = main_page.difference_visible_boxes_without_fix_the_cursor()
    assert initial_list_boxes[2] == list_boxes_without_fixing_the_cursor[0]
    assert initial_list_boxes[3] == list_boxes_without_fixing_the_cursor[1]


@allure.story('changing_visible_boxes_via_left_arrow')
def test_changing_visible_boxes_via_left_arrow(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    initial_list_boxes = main_page.visible_list_boxes()
    main_page.five_clicks_glide_arrow_left()
    list_boxes_after_glide = main_page.visible_list_boxes()
    assert initial_list_boxes != list_boxes_after_glide


@allure.story('changing_visible_boxes_via_right_arrow')
def test_changing_visible_boxes_via_right_arrow(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    initial_list_boxes = main_page.visible_list_boxes()
    main_page.five_clicks_glide_arrow_right()
    list_boxes_after_glide = main_page.visible_list_boxes()
    assert initial_list_boxes != list_boxes_after_glide


@pytest.mark.parametrize(
    "city",
    [('Lidzbark Warmiński',),
     ('Warszawa',),
     ('Gdynia',)]
)
@allure.story('possibility_of_delivery_to_a_certain_city')
def test_possibility_of_delivery_to_a_certain_city(driver, city):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.enter_place_of_delivery(city)
    main_page.click_button_zamow_on_place_of_delivery()
    order_page = OrderPage(driver)
    assert order_page.page_title == 'Zamówienie – Zamówienie Kuchnia Vikinga'


@pytest.mark.parametrize(
    "city",
    [('Ciechocinek',),
     ('Piła',),
     ('abrakadabra',),
     ('#2345#$%',)]
)
@allure.story('impossibility_of_delivery_to_a_certain_city')
def test_impossibility_of_delivery_to_a_certain_city(driver, city):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.enter_place_of_delivery(city)
    notice_of_impossibility = main_page.message_of_impossibility
    assert notice_of_impossibility == 'Nie dowozimy - zgłoś!'


@pytest.mark.parametrize(
    "part_name_city",
    [('Gd',),
     ('War',),
     ('Bi',),
     ('Lub',)
     ]
)
@allure.story('possibility_of_delivery_to_a_certain_city_by_partial_name')
def test_possibility_of_delivery_to_a_certain_city_by_partial_name(driver, part_name_city):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.partial_entry_of_delivery_location(part_name_city)
    main_page.click_button_zamow_on_place_of_delivery()
    order_page = OrderPage(driver)
    assert order_page.page_title == 'Zamówienie – Zamówienie Kuchnia Vikinga'


@pytest.mark.parametrize(
    "part_name_city",
    [('G',),
     ('W',),
     ('B',),
     ('L',)
     ]
)
@allure.story('impossibility_of_delivery_to_a_certain_city_by_single_letter')
def test_impossibility_of_delivery_to_a_certain_city_by_single_letter(driver, part_name_city):
    main_page = MainPage(driver)
    main_page.open_page()
    assert main_page.partial_entry_of_delivery_location(part_name_city) is True


@allure.story('open_page_ladies_vibes')
def test_open_page_ladies_vibes(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_ladies_vibes()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Najlepsza dieta odchudzająca dla kobiet - Kuchnia Vikinga'


@allure.story('open_page_wybor_menu')
def test_open_page_wybor_menu(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_wybor_menu()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Dieta pudełkowa z wyborem menu | Kuchnia Vikinga'


@allure.story('open_page_standard')
def test_open_page_standard(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_standard()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Dieta odchudzająca Standard - dla każdego | Kuchnia Vikinga'


@allure.story('open_page_active_pro')
def test_open_page_active_pro(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_active_pro()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Catering dietetyczny dla sportowców - Dieta Active Pro | Kuchnia Vikinga'


@allure.story('open_page_low_ig')
def test_open_page_low_ig(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_low_ig()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Dieta z niskim indeksem glikemicznym (ig) | Kuchnia Vikinga'


@allure.story('open_page_ketogeniczna')
def test_open_page_ketogeniczna(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_ketogeniczna()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Dieta pudełkowa keto (ketogeniczna) | Kuchnia Vikinga'


@allure.story('open_page_soft')
def test_open_page_soft(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_soft()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Dieta pudełkowa lekkostrawna lekka | Kuchnia Vikinga'


@allure.story('open_page_made_by_chef')
def test_open_page_made_by_chef(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_made_by_chef()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Dieta pudełkowa premium | Kuchnia Vikinga'


@allure.story('open_page_ekonomiczna')
def test_open_page_ekonomiczna(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_ekonomiczna()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Dieta pudełkowa 3 posiłki catering dla zabieganych | Kuchnia Vikinga'


@allure.story('open_page_bez_laktozy_i_glutenu')
def test_open_page_bez_laktozy_i_glutenu(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_bez_laktozy_i_glutenu()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Dieta pudełkowa bez laktozy i glutenu | Kuchnia Vikinga'


@allure.story('open_page_wege_ryby')
def test_open_page_wege_ryby(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_wege_ryby()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Dieta bez mięsa, wege z rybami | Kuchnia Vikinga'


@allure.story('open_page_ekonomiczna_wege')
def test_open_page_ekonomiczna_wege(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_ekonomiczna_wege()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Dieta pudełkowa wege, wegetariańska | Kuchnia Vikinga'


@allure.story('open_page_detoks_sokowy')
def test_open_page_detoks_sokowy(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_detoks_sokowy()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Dieta detoks sokowy oczyszczająca - catering | Kuchnia Vikinga'


@allure.story('open_page_hashimoto')
def test_open_page_hashimoto(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_hashimoto()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Hashimoto dieta pudełkowa bez glutenu ' \
                                    '(dieta przy niedoczynności tarczycy) | Kuchnia Vikinga'


@allure.story('open_page_weganska')
def test_open_page_weganska(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_weganska()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Dieta pudełkowa wegańska, catering | Kuchnia Vikinga'


@allure.story('open_page_progress')
def test_open_page_progress(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_progress()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Dieta pudełkowa dla par, dla zapracowanych | Kuchnia Vikinga'


@allure.story('open_page_fodmap')
def test_open_page_fodmap(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_fodmap()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Dieta low FODMAP - catering w jelicie drażliwym | Kuchnia Vikinga'


@allure.story('open_page_summer_vibes')
def test_open_page_summer_vibes(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_summer_vibes()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Summer Vibes - Kuchnia Vikinga'


@allure.story('open_page_wszystkie_diety')
def test_open_page_wszystkie_diety(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_wszystkie_diety()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Diety - Kuchnia Vikinga'


@allure.story('open_page_cennik')
def test_open_page_cennik(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.click_tab_cennik()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Cennik - Kuchnia Vikinga'


@allure.story('open_page_kontakt')
def test_open_page_kontakt(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.click_tab_kontakt()
    order_page = OrderPage(driver)
    assert order_page.page_title == 'Kontakt - Kuchnia Vikinga'


@allure.story('open_page_panel_clienta')
def test_open_page_panel_clienta(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.click_tab_panel_clienta()
    order_page = OrderPage(driver)
    assert order_page.page_title == 'Panel Klienta'


@allure.story('open_page_zamowienie')
def test_open_page_zamowienie(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.click_tab_zamow_teraz()
    order_page = OrderPage(driver)
    assert order_page.page_title == 'Zamówienie – Zamówienie Kuchnia Vikinga'


@allure.story('open_page_wszystkie_diety_button_poznaj_diety_vikinga')
def test_open_page_wszystkie_diety_button_poznaj_diety_vikinga(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_button_poznaj_diety_vikinga()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Diety - Kuchnia Vikinga'


@allure.story('open_page_wszystkie_diety_button_zobacz_nasze_diety')
def test_open_page_wszystkie_diety_button_zobacz_nasze_diety(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_tab_diety()
    main_page.click_button_zobacz_nasze_diety()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Diety - Kuchnia Vikinga'


@allure.story('open_page_menu')
def test_open_page_menu(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.click_tab_menu()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Menu - Kuchnia Vikinga'


@allure.story('open_page_delivery_option')
def test_open_page_delivery_option(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.click_tab_strefy_dostaw()
    other_page = OtherPage(driver)
    assert other_page.page_title == 'Strefy dostaw - Kuchnia Vikinga'
