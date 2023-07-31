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
calendar_days = (By.CSS_SELECTOR, '.calendar__day')

active_day = (By.CSS_SELECTOR, '.calendar__day--active')
ordering_days = (By.CSS_SELECTOR, 'input[placeholder="0"]')


