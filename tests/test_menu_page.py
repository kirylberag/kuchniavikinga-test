from pages.main_page import MainPage
from pages.menu_page import MenuPage


def test_open_main_page(driver):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    menu_page.click_logo()
    main_page = MainPage(driver)
    assert main_page.page_title == 'Zdrowy catering dietetyczny, dieta pudełkowa | Kuchnia Vikinga'


def test_day_is_correct(driver):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    day_on_page = menu_page.day_on_page()
    today = menu_page.day_real
    assert day_on_page == today


def test_date_is_correct(driver):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    date_on_page = menu_page.date_on_page()
    today = menu_page.date_real
    assert date_on_page == today


def test_correct_carousel_sliding(driver, difference=-1):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    menu_page.three_clicks_glide_arrow_left()
    menu_page.two_clicks_glide_arrow_right()
    day_on_page = menu_page.day_on_page()
    date_on_page = menu_page.date_on_page()
    new_day_on_page = menu_page.day_on_page(difference)
    new_date_on_page = menu_page.date_on_page(difference)
    assert day_on_page != new_day_on_page
    assert date_on_page != new_date_on_page


def test_correct_menu_display_summer_vibes(driver, dieta='meals_summer_vibes'):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    menu_page.click_field_menu()
    menu_page.click_menu_summer_vibes()
    meals = menu_page.meals(dieta)
    assert meals == ['Śniadanie', 'Drugie śniadanie', 'Obiad', 'Podwieczorek']


def test_correct_menu_display_ladies_vibes(driver, dieta='meals_ladies_vibes'):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    menu_page.click_field_menu()
    menu_page.click_menu_ladies_vibes()
    meals = menu_page.meals(dieta)
    assert meals == ['Śniadanie', 'Drugie śniadanie', 'Obiad', 'Podwieczorek', 'Kolacja']


def test_correct_menu_display_standard(driver, dieta='meals_standard'):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    menu_page.click_field_menu()
    menu_page.click_menu_standard()
    meals = menu_page.meals(dieta)
    assert meals == ['Śniadanie', 'Drugie śniadanie', 'Obiad', 'Podwieczorek', 'Kolacja']


def test_correct_menu_display_active_pro(driver, dieta='meals_active_pro'):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    menu_page.click_field_menu()
    menu_page.click_menu_active_pro()
    meals = menu_page.meals(dieta)
    assert meals == ['Śniadanie', 'Drugie śniadanie', 'Obiad', 'Podwieczorek', 'Kolacja']


def test_correct_menu_display_low_ig(driver, dieta='meals_low_ig'):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    menu_page.click_field_menu()
    menu_page.click_menu_low_ig()
    meals = menu_page.meals(dieta)
    assert meals == ['Śniadanie', 'Drugie śniadanie', 'Obiad', 'Podwieczorek', 'Kolacja']


def test_correct_menu_display_ketogeniczna(driver, dieta='meals_ketogeniczna'):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    menu_page.click_field_menu()
    menu_page.click_menu_ketogeniczna()
    meals = menu_page.meals(dieta)
    assert meals == ['Śniadanie', 'Obiad', 'Podwieczorek', 'Kolacja']


def test_correct_menu_display_soft(driver, dieta='meals_soft'):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    menu_page.click_field_menu()
    menu_page.click_menu_soft()
    meals = menu_page.meals(dieta)
    assert meals == ['Śniadanie', 'Drugie śniadanie', 'Obiad', 'Podwieczorek', 'Kolacja']


def test_correct_menu_display_made_by_chef(driver, dieta='meals_made_by_chef'):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    menu_page.click_field_menu()
    menu_page.click_menu_made_by_chef()
    meals = menu_page.meals(dieta)
    assert meals == ['Śniadanie', 'Drugie śniadanie', 'Obiad', 'Podwieczorek', 'Kolacja']


def test_correct_menu_display_ekonomiczna(driver, dieta='meals_ekonomiczna'):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    menu_page.click_field_menu()
    menu_page.click_menu_ekonomiczna()
    meals = menu_page.meals(dieta)
    assert meals == ['Śniadanie', 'Drugie śniadanie', 'Obiad']


def test_correct_menu_display_bez_laktozy_i_glutenu(driver, dieta='meals_bez_laktozy_i_glutenu'):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    menu_page.click_field_menu()
    menu_page.click_menu_bez_laktozy_i_glutenu()
    meals = menu_page.meals(dieta)
    assert meals == ['Śniadanie', 'Drugie śniadanie', 'Obiad', 'Podwieczorek', 'Kolacja']


def test_correct_menu_display_wege_ryby(driver, dieta='meals_wege_ryby'):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    menu_page.click_field_menu()
    menu_page.click_menu_wege_ryby()
    meals = menu_page.meals(dieta)
    assert meals == ['Śniadanie', 'Drugie śniadanie', 'Obiad', 'Podwieczorek', 'Kolacja']


def test_correct_menu_display_ekonomiczna_wege(driver, dieta='meals_ekonomiczna_wege'):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    menu_page.click_field_menu()
    menu_page.click_menu_ekonomiczna_wege()
    meals = menu_page.meals(dieta)
    assert meals == ['Śniadanie', 'Drugie śniadanie', 'Obiad']


def test_correct_menu_display_hashimoto(driver, dieta='meals_hashimoto'):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    menu_page.click_field_menu()
    menu_page.click_menu_hashimoto()
    meals = menu_page.meals(dieta)
    assert meals == ['Śniadanie', 'Drugie śniadanie', 'Obiad', 'Podwieczorek', 'Kolacja']


def test_correct_menu_display_weganska(driver, dieta='meals_weganska'):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    menu_page.click_field_menu()
    menu_page.click_menu_weganska()
    meals = menu_page.meals(dieta)
    assert meals == ['Śniadanie', 'Drugie śniadanie', 'Obiad', 'Podwieczorek', 'Kolacja']


def test_correct_menu_display_progress(driver, dieta='meals_progress'):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    menu_page.click_field_menu()
    menu_page.click_menu_progress()
    meals = menu_page.meals(dieta)
    assert meals == ['Obiad', 'Kolacja']


def test_correct_menu_display_fodmap(driver, dieta='meals_fodmap'):
    menu_page = MenuPage(driver)
    menu_page.open_page()
    menu_page.click_field_menu()
    menu_page.click_menu_fodmap()
    meals = menu_page.meals(dieta)
    assert meals == ['Śniadanie', 'Drugie śniadanie', 'Obiad', 'Podwieczorek', 'Kolacja']
