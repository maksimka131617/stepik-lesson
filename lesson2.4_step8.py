import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)   #price


    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button1 = browser.find_element(By.CSS_SELECTOR, "#book")
    button0 = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))
    button1.click()

    browser.execute_script("window.scrollBy(0, 1000);")

    input1 = browser.find_element_by_css_selector("#input_value")
    x = input1.text

    input2 = browser.find_element_by_css_selector("#answer")
    input2.send_keys(calc(x))


    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "solve")))

    button.click()

    # countdown





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()