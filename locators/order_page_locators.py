import allure
from selenium.webdriver.common.by import By


@allure.step('Локаторы первой станицы заказа')
class OrderPageLocators:

    #'Локаторы первой станицы заказа'
    inputs = (By.XPATH, '//input[contains(@class, "Input_Responsible__1jDKN")]')
    locator_button_zakazat_shapka = (By.XPATH, '//button[@class="Button_Button__ra12g"]') #Кнопка заказать в шапке сайта
    locator_button_zakazat_podval = [By.CLASS_NAME, 'Button_Button__ra12g'] #Кнопка заказать в подвале сайта
    locator_pole_name = (By.XPATH, '//input[contains(@placeholder, "* Имя")]') #Поле имя
    locator_pole_familia = (By.XPATH, '//input[contains(@placeholder, "* Фамилия")]') #Поле Фамилия
    locator_pole_adres = (By.XPATH, '// input[ @ placeholder = "* Адрес: куда привезти заказ"]') #Поле адрес
    locator_pole_metro = (By.XPATH, "//input[@placeholder='* Станция метро']") #Поле метро
    locator_metro_sokolniki = (By.XPATH, "//div[text()='Сокольники']")
    locator_pole_phone = (By.XPATH, '// input[ @ placeholder = "* Телефон: на него позвонит курьер"]') #Поле телефон
    locator_button_dalee = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]') #Кнопка Далее(для кого самокат)

    #'Локаторы второй станицы заказа'
    locarot_pole_kogda_privezti_samokat = (By.XPATH, '//input[@placeholder ="* Когда привезти самокат"]')
    locarot_pole_data = (By.XPATH, '//div[@class="react-datepicker__day react-datepicker__day--012"]')
    locator_pole_srok_arendi = (By.XPATH, '//div[@class="Dropdown-placeholder"]')
    locator_pole_srok_troe_sutok = (By.XPATH, "//div[text()='трое суток']")
    locator_checkbox_black = (By.XPATH, "//input[@id='black']")
    locator_comment = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    locator_knopka_zakazat = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    locator_button_Da = (By.XPATH, "//button[contains(text(), 'Да') and contains(@class, 'Button_Middle__1CSJM')]")
    locator_zakaz_oformlen = (By.XPATH, "//div[text()='Заказ оформлен']")

    locator_header_pro_arendu = (By.XPATH, "//div[@class='Order_Header__BZXOb']") #Заголовок Про Аренду

