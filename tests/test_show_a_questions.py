import allure
from pages.main_page import MainPage
import time


class Test_Vopros1:

    @allure.title('Когда нажимаешь на стрелочку первого вопроса, открывается соответствующий текст')
    def test_vopros_one(self, driver):
        main_page = MainPage(driver)
        driver.get('https://qa-scooter.praktikum-services.ru')
        time.sleep(1)
        main_page.click_question_one()
        time.sleep(1)
        assert main_page.get_answer_one() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

class Test_Vopros2:

    @allure.title('Когда нажимаешь на стрелочку второго вопроса, открывается соответствующий текст')
    def test_vopros_two(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru')
        time.sleep(2)
        main_page = MainPage(driver)
        main_page.click_question_two()
        time.sleep(2)
        assert main_page.get_answer_two() == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

class Test_Vopros3:

    @allure.title('Когда нажимаешь на стрелочку третьего вопроса, открывается соответствующий текст')
    def test_vopros_three(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru')
        time.sleep(2)
        main_page = MainPage(driver)
        main_page.click_question_three()
        time.sleep(2)
        assert main_page.get_answer_three() == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'


class Test_Vopros4:

    @allure.title('Когда нажимаешь на стрелочку четвертого вопроса, открывается соответствующий текст')
    def test_vopros_four(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru')
        time.sleep(2)
        main_page = MainPage(driver)
        main_page.click_question_four()
        time.sleep(2)
        assert main_page.get_answer_four() == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'


class Test_Vopros5:

    @allure.title('Когда нажимаешь на стрелочку пятого вопроса, открывается соответствующий текст')
    def test_vopros_five(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru')
        time.sleep(2)
        main_page = MainPage(driver)
        main_page.click_question_five()
        time.sleep(2)
        assert main_page.get_answer_five() == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'


class Test_Vopros6:

    @allure.title('Когда нажимаешь на стрелочку шестого вопроса, открывается соответствующий текст')
    def test_vopros_six(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru')
        time.sleep(2)
        main_page = MainPage(driver)
        main_page.click_question_six()
        time.sleep(2)
        assert main_page.get_answer_six() == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'


class Test_Vorpos7:

    @allure.title('Когда нажимаешь на стрелочку седьмого вопроса, открывается соответствующий текст')
    def test_vopros_seven(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru')
        time.sleep(2)
        main_page = MainPage(driver)
        main_page.click_question_seven()
        time.sleep(2)
        assert main_page.get_answer_seven() == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'


class Test_Vopros8:

    @allure.title('Когда нажимаешь на стрелочку восьмого вопроса, открывается соответствующий текст')
    def test_vopros_eight(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru')
        time.sleep(2)
        main_page = MainPage(driver)
        main_page.click_question_eight()
        time.sleep(2)
        assert main_page.get_answer_eight() == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

