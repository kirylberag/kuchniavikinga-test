from pages.base_page import BasePage
from locators import calorie_count_result_page_locators as CCRPL


class CalorieResultPage(BasePage):
    @property
    def reporting_calories_needed(self):
        text1 = self.find(CCRPL.text1).text
        text2 = self.find(CCRPL.text2).text
        text3 = self.find(CCRPL.text3).text
        text4 = self.find(CCRPL.text4).text
        return [f'{text1}\n{text2}\n{text3}\n{text4}', int(text3[:-4])]

    def calorie_count_check(self, wzrost, masa, wiek, intensity, goal):
        if goal == 1:
            text = 'schudnąć'
            numb = -700
        if goal == 2:
            text = 'utrzymać wagę'
            numb = 0
        if goal == 3:
            text = 'przytyć'
            numb = 700
        if not goal:
            text = ''
            numb = 0
        if not intensity:
            return (
                f'Poznaj nasze diety\n'
                f'Twoje zapotrzebowanie kaloryczne wynosi:\n'
                f'0 kcal\n'
                f'Aby {text}, wybierz jedną z poniższych diet w kaloryczności około {numb} kcal'
            )
        if wzrost is str(wzrost):
            if not wzrost[0].isdigit():
                wzrost = 0
            else:
                for i in range(len(wzrost)):
                    if wzrost[i].isdigit():
                        continue
                    else:
                        number_index = i
                        wzrost = int(wzrost[:number_index])
                        break
        if masa is str(masa):
            if not masa[0].isdigit():
                masa = 0
            else:
                for i in range(len(masa)):
                    if masa[i].isdigit():
                        continue
                    else:
                        number_index = i
                        masa = int(masa[:number_index])
                        break
        if wiek is str(wiek):
            if not wiek[0].isdigit():
                wiek = 0
            else:
                for i in range(len(wiek)):
                    if wiek[i].isdigit():
                        continue
                    else:
                        number_index = i
                        wiek = int(wiek[:number_index])
                        break
        cal = round((9.99 * masa + 6.242 * wzrost - 4.92 * wiek + 5) * intensity)
        if abs(self.reporting_calories_needed[1]) * 0.95 <= abs(cal) <= abs(self.reporting_calories_needed[1]) * 1.05:
            cal = self.reporting_calories_needed[1]
        return (
            f'Poznaj nasze diety\n'
            f'Twoje zapotrzebowanie kaloryczne wynosi:\n'
            f'{cal} kcal\n'
            f'Aby {text}, wybierz jedną z poniższych diet w kaloryczności około {cal + numb} kcal'
        )
