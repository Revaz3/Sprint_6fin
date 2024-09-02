import allure

from pages.main_page import MainPage
from conftest import driver



class TestSamokatButton:
    @allure.step('Проверка кнопки Самокат')
    def test_button_samokat(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru')
        main_page = MainPage(driver)
        main_page.click_button_samokat()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.step('Проверка кнопки Яндекс')
    class TestYandexButton:
        def test_button_yandex(self, driver):
            driver.get('https://qa-scooter.praktikum-services.ru')
            main_page = MainPage(driver)
            main_page.click_button_yandex()
            assert driver.current_url == 'https://dzen.ru/?yredirect=true'