import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
import time
from conftest import driver
from locators.order_page_locators import OrderPageLocators




class Test_Order:
    @allure.description('Кнопка «Заказать» вверху страницы')
    def test_order_one(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru')
        time.sleep(1)
        order_page = OrderPage(driver)
        order_page.click_button_zakazat()
        time.sleep(1)
        order_page.set_pole_name()
        order_page.set_pole_family()
        order_page.set_pole_address()
        order_page.click_pole_metro()
        time.sleep(1)
        order_page.set_metro_sokolniki()
        order_page.set_phone_number()
        order_page.click_button_dalee()
        time.sleep(1)
        order_page.set_pole_KogdePriveztiSamokat()
        time.sleep(1)
        order_page.click_data()
        time.sleep(1)
        order_page.click_pole_SrokArendi()
        time.sleep(1)
        order_page.set_pole_SrokArendi()
        time.sleep(1)
        order_page.click_pole_CvetSamokata()
        time.sleep(1)
        order_page.set_pole_Komment()
        time.sleep(1)
        order_page.click_button_Zakazat()
        time.sleep(1)
        order_page.click_button_Da()
        time.sleep(1)
        assert order_page.order_has_been_placed_text().startswith('Заказ оформле')


    @allure.description('Кнопка «Заказать» внизу страницы')
    def test_order_two(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru')
        time.sleep(1)
        main_page = MainPage(driver)
        time.sleep(1)
        main_page.click_button_podval()
        time.sleep(1)
        order_page = OrderPage(driver)
        order_page.set_pole_name_ivan()
        time.sleep(1)
        order_page.set_pole_family_ivanov()
        order_page.set_pole_address_two()
        order_page.click_pole_metro()
        time.sleep(1)
        order_page.set_metro_vikhino()
        order_page.set_phone_number_two()
        order_page.click_button_dalee()
        time.sleep(1)
        order_page.set_pole_KogdePriveztiSamokat()
        time.sleep(1)
        order_page.click_data()
        time.sleep(1)
        order_page.click_pole_SrokArendi()
        time.sleep(1)
        order_page.set_pole_SrokArendi()
        time.sleep(1)
        order_page.click_pole_CvetSamokata()
        time.sleep(1)
        order_page.set_pole_Komment()
        order_page.click_button_Zakazat()
        order_page.click_button_Da()
        time.sleep(1)
        assert order_page.order_has_been_placed_text().startswith('Заказ оформле')









