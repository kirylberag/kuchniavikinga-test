from pages.base_page import BasePage
from locators import main_page_locators as MPL
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import allure


@allure.feature('Main Page')
class MainPage(BasePage):
    page_url = '/'
    beginning_url = ''

    @property
    @allure.step('Display page title')
    def page_title(self):
        return self.driver.title

    @allure.step('Open the diet page')
    def open_tab_diety(self):
        self.find(MPL.tab_diety).click()

    @allure.step('Choose a diet - ladies vibes')
    def click_ladies_vibes(self):
        self.find(MPL.button_ladies_vibes).click()

    @allure.step('Open the menu page')
    def click_wybor_menu(self):
        self.find(MPL.button_wybor_menu).click()

    @allure.step('Selecting the standard menu')
    def click_standard(self):
        self.find(MPL.button_standard).click()

    @allure.step('Selecting the active pro menu')
    def click_active_pro(self):
        self.find(MPL.button_active_pro).click()

    @allure.step('Selecting the low ig menu')
    def click_low_ig(self):
        self.find(MPL.button_low_ig).click()

    @allure.step('Selecting the ketogeniczna menu')
    def click_ketogeniczna(self):
        self.find(MPL.button_ketogeniczna).click()

    @allure.step('Selecting the soft menu')
    def click_soft(self):
        self.find(MPL.button_soft).click()

    @allure.step('Selecting the made by chef menu')
    def click_made_by_chef(self):
        self.find(MPL.button_made_by_chef).click()

    @allure.step('Selecting the ekonomiczna menu')
    def click_ekonomiczna(self):
        self.find(MPL.button_ekonomiczna).click()

    @allure.step('Selecting bez laktozy i glutenu menu')
    def click_bez_laktozy_i_glutenu(self):
        self.find(MPL.button_bez_laktozy_i_glutenu).click()

    @allure.step('Selecting wege ryby menu')
    def click_wege_ryby(self):
        self.find(MPL.button_wege_ryby).click()

    @allure.step('Selecting ekonomiczna wege menu')
    def click_ekonomiczna_wege(self):
        self.find(MPL.button_ekonomiczna_wege).click()

    @allure.step('Selecting detoks sokowy menu')
    def click_detoks_sokowy(self):
        self.find(MPL.button_detoks_sokowy).click()

    @allure.step('Selecting the hashimoto menu')
    def click_hashimoto(self):
        self.find(MPL.button_hashimoto).click()

    @allure.step('Selecting weganska menu')
    def click_weganska(self):
        self.find(MPL.button_weganska).click()

    @allure.step('Selecting progress menu')
    def click_progress(self):
        self.find(MPL.button_progress).click()

    @allure.step('Selecting fodmap menu')
    def click_fodmap(self):
        self.find(MPL.button_fodmap).click()

    @allure.step('Selecting summer vibes menu')
    def click_summer_vibes(self):
        self.find(MPL.button_summer_vibes).click()

    @allure.step('Opening a page of all diets')
    def click_wszystkie_diety(self):
        self.find(MPL.button_wszystkie_diety).click()

    @allure.step('Opening the page of all prices')
    def click_tab_cennik(self):
        self.find(MPL.tab_cennik).click()

    @allure.step('Opening a page of all menus')
    def click_tab_menu(self):
        self.find(MPL.tab_menu).click()

    @allure.step('Opening the page of all delivery points')
    def click_tab_strefy_dostaw(self):
        self.find(MPL.tab_strefy_dostaw).click()

    @allure.step('Opening the menu of all delivery points')
    def open_tab_swiat_vikinga(self):
        self.find(MPL.tab_swiat_vikinga).click()

    @allure.step('Opening the menu projekt bez ocen')
    def click_projekt_bez_ocen(self):
        self.find(MPL.button_projekt_bez_ocen).click()

    @allure.step('Opening the menu dodatki do menu')
    def click_dodatki_do_menu(self):
        self.find(MPL.button_dodatki_do_menu).click()

    @allure.step('Opening the menu druzyna vikinga')
    def click_druzyna_vikinga(self):
        self.find(MPL.button_druzyna_vikinga).click()

    @allure.step('Opening the menu wiesci ze swiata vikinga')
    def click_wiesci_ze_swiata_vikinga(self):
        self.find(MPL.button_wiesci_ze_swiata_vikinga).click()

    @allure.step('Opening the menu punkty stacjonarne vikinga')
    def click_punkty_stacjonarne_vikinga(self):
        self.find(MPL.button_punkty_stacjonarne_vikinga).click()

    @allure.step('Opening the kontakt page')
    def click_tab_kontakt(self):
        self.find(MPL.tab_kontakt).click()

    @allure.step('Opening the menu panel clienta')
    def click_tab_panel_clienta(self):
        self.find(MPL.tab_panel_clienta).click()

    @allure.step('Click order now')
    def click_tab_zamow_teraz(self):
        self.find(MPL.tab_zamow_teraz).click()

    @allure.step('Pressing the all diets button')
    def click_button_poznaj_diety_vikinga(self):
        self.find(MPL.button_poznaj_diety_vikinga).click()

    @allure.step('Pressing the all diets button')
    def click_button_zobacz_nasze_diety(self):
        self.find(MPL.button_zobacz_nasze_diety).click()

    @allure.step('Visible diets on the slide')
    def visible_list_boxes(self):
        all_boxes = self.find_all(MPL.slider_boxes)
        visible_boxes = list()
        for box in all_boxes:
            if box.is_displayed():
                visible_boxes.append(box)
        return visible_boxes

    @allure.step('Press the left arrow 5 times')
    def five_clicks_glide_arrow_left(self):
        for i in range(5):
            self.find(MPL.glide_arrow_left).click()

    @allure.step('Press the right arrow 5 times')
    def five_clicks_glide_arrow_right(self):
        for i in range(5):
            self.find(MPL.glide_arrow_right).click()

    @allure.step('Lock the carousel with the cursor')
    def identical_visible_boxes_after_fixed_the_cursor(self):
        visible_boxes = self.visible_list_boxes()
        ActionChains(self.driver).move_to_element(visible_boxes[0]).pause(5).perform()
        visible_boxes_after_pause = self.visible_list_boxes()
        return visible_boxes_after_pause

    @allure.step('Waiting for slide scrolling')
    def difference_visible_boxes_without_fix_the_cursor(self):
        ActionChains(self.driver).pause(5).perform()
        visible_boxes_after_pause = self.visible_list_boxes()
        return visible_boxes_after_pause

    @allure.step('Calorie counting and result output')
    def calorie_counting(self, sex, wzrost, masa, wiek, intensity, goal):
        if sex == 1:
            self.find(MPL.button_kobieta).click()
        if sex == 2:
            self.find(MPL.button_mezczyzna).click()
        if wzrost or wzrost == 0:
            self.find(MPL.field_wzrost).send_keys(wzrost)
        if masa or masa == 0:
            self.find(MPL.field_masa).send_keys(masa)
        if wiek or wiek == 0:
            self.find(MPL.field_wiek).send_keys(wiek)
        if intensity:
            self.find(MPL.field_aktywnosc_fizyczna).click()
            if intensity == 1.4:
                self.find(MPL.button_cwicze_niewiele).click()
            if intensity == 1.5:
                self.find(MPL.button_cwicze_umiarkowanie).click()
            if intensity == 1.7:
                self.find(MPL.button_cwicze_dosc_intensywnie).click()
            if intensity == 1.9:
                self.find(MPL.button_cwicze_ciezko).click()
            if intensity == 2.2:
                self.find(MPL.button_cwicze_bardzo_ciezko).click()
        if goal:
            self.find(MPL.field_goal).click()
            if goal == 1:
                self.find(MPL.field_schudnac).click()
            if goal == 2:
                self.find(MPL.field_utrzymac_wage).click()
            if goal == 3:
                self.find(MPL.field_przytyc).click()
        self.find(MPL.button_znajdz_swoja_diete).click()
        if (not wzrost and wzrost != 0) or (not masa and masa != 0) or (not wiek and wiek != 0):
            return Alert(self.driver).text

    @allure.step('Pressing the delivery address button')
    def enter_place_of_delivery(self, city):
        self.find(MPL.field_gdzie_dowozi).send_keys(city)

    @allure.step('Pressing the order button on the delivery address')
    def click_button_zamow_on_place_of_delivery(self):
        self.find(MPL.button_zamow).click()

    @allure.step('Entering a city name')
    def partial_entry_of_delivery_location(self, part_name_city):
        self.find(MPL.field_gdzie_dowozi).send_keys(part_name_city)
        try:
            self.find(MPL.button_city).click()
        except:
            return True

    @property
    @allure.step('Message that delivery is not possible')
    def message_of_impossibility(self):
        text_message = self.find(MPL.field_message_of_possibility).text
        return text_message
