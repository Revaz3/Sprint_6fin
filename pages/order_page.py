import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик по кнопке заказать в шапке сайта')
    def click_button_zakazat(self):
        self.driver.find_element(*OrderPageLocators.locator_button_zakazat_shapka).click() #Клик по кнопке заказть


    @allure.step('Ввод имени Марк')
    def set_pole_name(self):
        self.driver.find_elements(*OrderPageLocators.inputs)[0].send_keys('Марк')

    @allure.step('Ввод имени Иван')
    def set_pole_name_ivan(self):
        self.driver.find_elements(*OrderPageLocators.inputs)[0].send_keys('Иван')

    @allure.step('Ввод фамилии Петров')
    def set_pole_family(self):
        self.driver.find_elements(*OrderPageLocators.inputs)[1].send_keys('Петров')

    @allure.step('Ввод фамилии Иванов')
    def set_pole_family_ivanov(self):
        self.driver.find_elements(*OrderPageLocators.inputs)[1].send_keys('Иванов')

    @allure.step('Ввод адреса доставки')
    def set_pole_address(self):
        self.driver.find_elements(*OrderPageLocators.inputs)[2].send_keys('Москва, Ленинградское шоссе 43с1')

    @allure.step('Ввод адреса доставки 2')
    def set_pole_address_two(self):
        self.driver.find_elements(*OrderPageLocators.inputs)[2].send_keys('Москва, Ленинградское шоссе 50с1')

    @allure.step('Клик по полю метро')
    def click_pole_metro(self):
        self.driver.find_element(*OrderPageLocators.locator_pole_metro).click()

    @allure.step('Заполняем поле "Метро Сокольники"')
    def set_metro_sokolniki(self):
        self.driver.find_element(By.XPATH, "//div[text()='Сокольники']").click()

    @allure.step('Заполняем поле "Метро Выхино"')
    def set_metro_vikhino(self):
        self.driver.find_element(By.XPATH, "//div[text()='Бульвар Рокоссовского']").click()

    @allure.step('Ввод номера телефона')
    def set_phone_number(self):
        self.driver.find_element(*OrderPageLocators.locator_pole_phone).send_keys("79631133444")

    @allure.step('Ввод номера телефона-2')
    def set_phone_number_two(self):
        self.driver.find_element(*OrderPageLocators.locator_pole_phone).send_keys("79631154344")

    @allure.step('Клик по кнопке далее')
    def click_button_dalee(self):
        self.driver.find_element(*OrderPageLocators.locator_button_dalee).click()

    @allure.step('Клик по полю дата аренды')
    def set_pole_KogdePriveztiSamokat(self):
        self.driver.find_element(*OrderPageLocators.locarot_pole_kogda_privezti_samokat).click()

    @allure.step('выбор даты аренды')
    def click_data(self):
        self.driver.find_element(*OrderPageLocators.locarot_pole_data).click()

    @allure.step('Клик по полю срок аренды')
    def click_pole_SrokArendi(self):
        self.driver.find_element(*OrderPageLocators.locator_pole_srok_arendi).click()

    @allure.step('Выбор срока аренды')
    def set_pole_SrokArendi(self):
        self.driver.find_element(*OrderPageLocators.locator_pole_srok_troe_sutok).click()

    @allure.step('Клик по чекбоксе Цвет самоката')
    def click_pole_CvetSamokata(self):
        self.driver.find_element(*OrderPageLocators.locator_checkbox_black).click()

    def set_pole_Komment(self):
        self.driver.find_element(*OrderPageLocators.locator_comment).send_keys("Привет")

    @allure.step('Клик по кнопке Заказать')
    def click_button_Zakazat(self):
        self.driver.find_element(*OrderPageLocators.locator_knopka_zakazat).click()

    @allure.step('Клик по кнопке ДА')
    def click_button_Da(self):
        self.driver.find_element(*OrderPageLocators.locator_button_Da).click()

    @allure.step('Получить текст Заказ оформлен')
    def order_has_been_placed_text(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.locator_zakaz_oformlen)).text











