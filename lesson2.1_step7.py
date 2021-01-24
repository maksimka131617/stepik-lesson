from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input2 = browser.find_element_by_css_selector("#input_value")
    x = input2.text
    print(x)

    res = calc(x)

    input3 = browser.find_element_by_css_selector("#answer")
    input3.send_keys(res)

    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()

    radiobox = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobox)
    radiobox.click()

    button = browser.find_element_by_css_selector("body > div > form > button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()