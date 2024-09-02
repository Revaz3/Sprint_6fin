from selenium.webdriver.common.by import By


class MainPageLocators:

    locator_question_one_element = [By.ID, 'accordion__heading-0'] #Вопрос 1
    locator_question_two_element = [By.ID, 'accordion__heading-1'] #Вопрос 2
    locator_question_three_element = [By.ID, 'accordion__heading-2'] #Вопрос 3
    locator_question_four_element = [By.ID, 'accordion__heading-3'] #Вопрос 4
    locator_question_five_element = [By.ID, 'accordion__heading-4'] #Вопрос 5
    locator_question_six_element = [By.ID, 'accordion__heading-5'] #Вопрос 6
    locator_question_seven_element = [By.ID, 'accordion__heading-6'] #Вопрос 7
    locator_question_eight_element = [By.ID, 'accordion__heading-7'] #Вопрос 8

    locator_answer_one_element = [[By.ID, 'accordion__panel-0']] #Ответ на вопрос 1
    locator_answer_two_element = [By.ID, 'accordion__panel-1'] #Ответ на вопрос 2
    locator_answer_three_element = [By.ID, 'accordion__panel-2'] #Ответ на вопрос 3
    locator_answer_four_element = [By.ID, 'accordion__panel-3'] #Ответ на вопрос 4
    locator_answer_five_element = [By.ID, 'accordion__panel-4'] #Ответ на вопрос 5
    locator_answer_six_element = [By.ID, 'accordion__panel-5'] #Ответ на вопрос 6
    locator_answer_seven_element = [By.ID, 'accordion__panel-6'] #Ответ на вопрос 7
    locator_answer_eight_element = [By.ID, 'accordion__panel-7'] #Ответ на вопрос 8

    locator_button_podval = [By.CLASS_NAME, 'Button_Button__ra12g'] #Кнопка заказать внизу страницы
    locator_button_samokat = (By.XPATH, '//a[@class= "Header_LogoScooter__3lsAR"]') #Кнопка Самокат логотип
    locator_button_yandex = (By.XPATH, '//a[@class= "Header_LogoYandex__3TSOI"]') #Кнопка Яндекс логотип