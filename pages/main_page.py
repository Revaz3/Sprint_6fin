import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators



class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик по первому вопросу')
    def click_question_one(self):
        last_element = self.driver.find_element(*MainPageLocators.locator_question_eight_element)
        self.driver.execute_script('arguments[0].scrollIntoView();', last_element)
        element = WebDriverWait(self.driver, 80).until(EC.visibility_of_element_located(MainPageLocators.locator_question_one_element))
        element.click()

    @allure.step('Клик по второму вопросу')
    def click_question_two(self):
        last_element = self.driver.find_element(*MainPageLocators.locator_question_eight_element)
        self.driver.execute_script('arguments[0].scrollIntoView();', last_element)
        element = WebDriverWait(self.driver, 80).until(EC.visibility_of_element_located(MainPageLocators.locator_question_two_element))
        element.click()

    @allure.step('Клик по третьему вопросу')
    def click_question_three(self):
        last_element = self.driver.find_element(*MainPageLocators.locator_question_eight_element)
        self.driver.execute_script('arguments[0].scrollIntoView();', last_element)
        element = WebDriverWait(self.driver, 80).until(EC.visibility_of_element_located(MainPageLocators.locator_question_three_element))
        element.click()

    @allure.step('Клик по четвертому вопросу')
    def click_question_four(self):
        last_element = self.driver.find_element(*MainPageLocators.locator_question_eight_element)
        self.driver.execute_script('arguments[0].scrollIntoView();', last_element)
        element = WebDriverWait(self.driver, 80).until(EC.visibility_of_element_located(MainPageLocators.locator_question_four_element))
        element.click()

    @allure.step('Клик по пятому вопросу')
    def click_question_five(self):
        last_element = self.driver.find_element(*MainPageLocators.locator_question_eight_element)
        self.driver.execute_script('arguments[0].scrollIntoView();', last_element)
        element = WebDriverWait(self.driver, 80).until(EC.visibility_of_element_located(MainPageLocators.locator_question_five_element))
        element.click()

    @allure.step('Клик по шестому вопросу')
    def click_question_six(self):
        last_element = self.driver.find_element(*MainPageLocators.locator_question_eight_element)
        self.driver.execute_script('arguments[0].scrollIntoView();', last_element)
        element = WebDriverWait(self.driver, 80).until(EC.visibility_of_element_located(MainPageLocators.locator_question_six_element))
        element.click()

    @allure.step('Клик по седьмому вопросу')
    def click_question_seven(self):
        last_element = self.driver.find_element(*MainPageLocators.locator_question_eight_element)
        self.driver.execute_script('arguments[0].scrollIntoView();', last_element)
        element = WebDriverWait(self.driver, 80).until(EC.visibility_of_element_located(MainPageLocators.locator_question_seven_element))
        element.click()

    @allure.step('Клик по восьмому вопросу')
    def click_question_eight(self):
        last_element = self.driver.find_element(*MainPageLocators.locator_question_eight_element)
        self.driver.execute_script('arguments[0].scrollIntoView();', last_element)
        element = WebDriverWait(self.driver, 80).until(EC.visibility_of_element_located(MainPageLocators.locator_question_eight_element))
        element.click()





    @allure.step('Ответ на первый вопрос')
    def get_answer_one(self):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(*MainPageLocators.locator_answer_one_element)).text

    @allure.step('Ответ на второй вопрос')
    def get_answer_two(self):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(MainPageLocators.locator_answer_two_element)).text

    @allure.step('Ответ на третий вопрос')
    def get_answer_three(self):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(MainPageLocators.locator_answer_three_element)).text

    @allure.step('Ответ на четвертый вопрос')
    def get_answer_four(self):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(MainPageLocators.locator_answer_four_element)).text

    @allure.step('Ответ на пятый вопрос')
    def get_answer_five(self):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(MainPageLocators.locator_answer_five_element)).text

    @allure.step('Ответ на шестой вопрос')
    def get_answer_six(self):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(MainPageLocators.locator_answer_six_element)).text

    @allure.step('Ответ на седьмой вопрос')
    def get_answer_seven(self):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(MainPageLocators.locator_answer_seven_element)).text

    @allure.step('Ответ на восьмой вопрос')
    def get_answer_eight(self):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(MainPageLocators.locator_answer_eight_element)).text

    @allure.step('Клик по кнопке заказать внизу страницы')
    def click_button_podval(self):
        self.driver.find_element(*MainPageLocators.locator_button_podval).click()

    @allure.step('Клик по кнопке Самоката логотип')
    def click_button_samokat(self):
        self.driver.find_element(*MainPageLocators.locator_button_samokat).click()

    @allure.step('Клик по кнопке Яндекс логотип')
    def click_button_yandex(self):
        self.driver.find_element(*MainPageLocators.locator_button_yandex).click()

