import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/file_input.html"
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    browser = webdriver.Chrome()
    browser.get(link)





    input1 = browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys('Max')

    input2 = browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys('Mayfet')

    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys('lizamee@mail.ru')

    element = browser.find_element_by_css_selector("#file")
    element.send_keys(file_path)

    option2 = browser.find_element_by_css_selector("[class='btn btn-primary']")
    option2.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()