from selenium.webdriver.common.by import By


icon_logo = (By.CLASS_NAME, 'custom-logo-link')
step_order = (By.CSS_SELECTOR, '.steps-page-progress__item')
button_choice_diet = (By.CSS_SELECTOR, '.button-m')
list_cities = (By.CSS_SELECTOR, '.combobox-cities-menu')
field_enter_city = (By.ID, 'combobox-cities-toggle-button')
enter_city = (By.ID, 'combobox-cities-input')
city_context = (By.ID, 'combobox-cities-item-0')
text_empty_city = (By.CSS_SELECTOR, '.dds-combobox__item--empty')
popular_cities = (By.CSS_SELECTOR, '.cypress-city')
indicator_text = (By.CSS_SELECTOR, '.dds-combobox__label')
choice_menu = (By.CSS_SELECTOR, '.button-blank')
text_menu = (By.CSS_SELECTOR, '.type-of-program__card-top')
number_of_steps = (By.CSS_SELECTOR, '.box-step__title')
choice_diet = (By.CSS_SELECTOR, '.diet-card')
calorie_count = (By.CSS_SELECTOR, '.min-width-130')
all_diets = (By.CSS_SELECTOR, '.diet-card__name')
all_calories = (By.CSS_SELECTOR, '.min-width-130')
choice_sex_men = (By.ID, 'male')
choice_sex_women = (By.ID, 'female')
button_next = (By.CSS_SELECTOR, '.calculator-modal__footer-modal-button')
field_age = (By.XPATH, '//*[@name = "age"]')
field_weight = (By.XPATH, '//*[@name = "weight"]')
field_height = (By.XPATH, '//*[@name = "height"]')
button_next2 = (By.CSS_SELECTOR, '.button-icon-right')
button_back2 = (By.CSS_SELECTOR, '.fa-arrow-left')
field_activity = (By.CSS_SELECTOR, '.calculator-modal__card-checkbox')
result_calorie = (By.CSS_SELECTOR, '.spacer-bottom-24')
button_accept = (By.XPATH, '//*[@class="button-label "]')
numb_calories = (By.CSS_SELECTOR, '.spacer-bottom-24')
button_accept_calories = (By.CSS_SELECTOR, '.button-icon-right')
indicator_text2 = (By.CSS_SELECTOR, '.h300')
indicator_text3 = (By.CSS_SELECTOR, 'calculator-modal__close')
name_diets_standard = (By.CSS_SELECTOR, '.diet-card__name')
description_diets = (By.CSS_SELECTOR, '.diet-card__more')
name_description_diets = (By.CSS_SELECTOR, '.diet-description-and-menu-modal__title')
day_today = (By.CSS_SELECTOR, '.spacer-bottom-16.color-gray-400')
date_today = (By.CSS_SELECTOR, '.catering-menu__date')
diets_standard = (By.CSS_SELECTOR, '.diet-card__select')
calories = (By.CSS_SELECTOR, '.cypress-calorie')
meal = (By.CSS_SELECTOR, '.cypress-meal')
message_via_minimal = (By.CSS_SELECTOR, '.body-l.spacer-bottom-16')
button_accept_message_minimal_meals = (
    By.XPATH, '//*[@class="custom-modal-another-catering__buttons justify-content-flex-end"]//*[@class="button-label "]'
)
message_number_of_meals_selected = (By.CSS_SELECTOR, '.color-gray-800')
next_step = (By.CSS_SELECTOR, '.button.button-block.button-icon-right.button-l')
order_detail_message = (By.CSS_SELECTOR, '.box-step__title')
saturday_delivery_button = (By.ID, 'saturdays')
sunday_delivery_button = (By.ID, 'sundays')
number_of_weeks = (By.CSS_SELECTOR, '.calendar__week')
blocked_weekends = (By.CSS_SELECTOR, '.calendar__day--locked')
active_days = (By.CSS_SELECTOR, '.calendar__day.no-select:not(.calendar__day--locked):not(.calendar__day--past)')
ordering_days = (By.CSS_SELECTOR, 'input[placeholder="0"]')
selected_days = (By.CSS_SELECTOR, '.calendar__day--active')
numbers_days = (By.CSS_SELECTOR, 'span.label-m')
button_next3 = (By.CSS_SELECTOR, '.button-label')
text_step3 = (By.CSS_SELECTOR, '.box-step__flex-breaker')
additive_selection_button = (By.CSS_SELECTOR, '.color-primary.button-blank.button')
additive_button = (
    By.CSS_SELECTOR, '.button.amount-carousel__without-padding.button-clean.button-no-label[type="button"]'
)
button_additive_next = (By.CSS_SELECTOR, '.button.button-m.button-primary')
amount_of_additives = (By.CSS_SELECTOR, 'p[class="label-m"]')
button_next4 = (By.CSS_SELECTOR, '.button.spacer-top-24.button-block.button-icon-right.button-m')
numbers_selected_days = (By.CSS_SELECTOR, '[placeholder = "0"]')
step4_ordering_days = (By.CSS_SELECTOR, '.shopping-cart-item__days')
message_for_supplements = (By.CSS_SELECTOR, '.shopping-cart-item__adds-on-desktop')
diet_message = (By.CSS_SELECTOR, '.shopping-cart-item__title-wrapper')
button_next5 = (By.CSS_SELECTOR, '.button.spacer-top-24.button-block.button-icon-right.button-m')
confirmation_button_to_continue_as_a_guest = (By.CSS_SELECTOR, '.button.button-clean.button-m')
continue_button_without_registration = (By.CSS_SELECTOR, '.button.button-blank.button-l')
first_name = (By.ID, 'name')
first_name_error = (By.XPATH, "//*[contains(text(), 'Imię jest wymagane')]")
second_name = (By.ID, 'surname')
second_name_error = (By.XPATH, "//*[contains(text(), 'Nazwisko jest wymagane')]")
email = (By.ID, 'email')
email_error = (By.XPATH, "//*[contains(text(), 'Email jest wymagany')]")
email_error2 = (By.XPATH, "//*[contains(text(), 'Wpisz poprawny adres email')]")
email_error3 = (By.XPATH, "//*[contains(text(), 'Adres email nie może zawierać spacji')]")
phone_number = (By.CSS_SELECTOR, '[name="phone"]')
phone_number_error = (By.XPATH, "//*[contains(text(), 'Telefon jest wymagany')]")
phone_number_error2 = (By.XPATH, "//*[contains(text(), 'Wprowadź poprawny numer (np. 123456789)')]")
field_index = (By.ID, 'combobox-zip-codes-input')
select_index = (By.ID, 'combobox-zip-codes-item-0')
index_error = (By.CSS_SELECTOR, '.color-error.body-m.spacer-top-4.steps-page-third__small-input')
street = (By.ID, 'street')
street_error = (By.XPATH, "//*[contains(text(), 'Ulica jest wymagana')]")
house_number = (By.ID, 'buildingNumber')
house_number_error = (By.XPATH, "//*[contains(text(), 'Numer domu jest wymagany')]")
floor_number = (By.ID, 'floor')
floor_number_error = (By.XPATH, "//*[contains(text(), 'Numer piętra jest za długi')]")
stairwell_number = (By.ID, 'gate')
stairwell_number_error = (By.XPATH, "//*[contains(text(), 'Numer klatki jest za długi')]")
field_delivery_time = (By.CSS_SELECTOR, '.select__selectedItem-icon.select__selectedItem-icon-select-link')
select_delivery_time = (By.ID, 'deliveryHour-item-0')
delivery_time_error = (By.CSS_SELECTOR, '.color-error.body-m.spacer-top-4.spacer-bottom-24')
privacy_policy_consent = (By.ID, 'regulationsCatering')
pay_button = (By.CSS_SELECTOR, '.button.button-block.button-icon-right.button-m')
finish_indicator = (By.CSS_SELECTOR, '.tpay-pay')
