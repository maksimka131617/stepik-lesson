from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector("body > div > form > div.form-group > label > span:nth-child(1)")
    input2 = browser.find_element_by_css_selector("#input_value")
    io = input1.text
    x = input2.text

    x1 = io.replace('What is ','')
    x2 = x1.replace(', where x =', '')
    res = calc(x)

    input3 = browser.find_element_by_css_selector("#answer")
    input3.send_keys(res)

    option1 = browser.find_element_by_css_selector("body > div > form > div.form-check.form-check-custom > label")
    option1.click()

    option2 = browser.find_element_by_css_selector("body > div > form > div.form-check.form-radio-custom > label")
    option2.click()

    button = browser.find_element_by_css_selector("body > div > form > button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()