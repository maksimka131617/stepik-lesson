import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input2 = browser.find_element_by_css_selector("#num1")
    input1 = browser.find_element_by_css_selector("#num2")

    x = input2.text
    y = input1.text
    z = int(x) + int(y)

    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_value(str(z))

    option2 = browser.find_element_by_css_selector("body > div > form > button")
    option2.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()