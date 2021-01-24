import time
import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    option2 = browser.find_element_by_css_selector("[class='trollface btn btn-primary']")
    option2.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    input1 = browser.find_element_by_css_selector("#input_value")
    x = input1.text

    input2 = browser.find_element_by_css_selector("#answer")
    input2.send_keys(calc(x))

    option2 = browser.find_element_by_css_selector("[class='btn btn-primary']")
    option2.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()