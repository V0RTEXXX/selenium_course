import math
from selenium import webdriver
import time
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element_by_class_name('trollface.btn.btn-primary')
    button1.click()
    new_window = browser.window_handles[1]
    print(new_window)
    browser.switch_to.window(new_window)
    input1 = browser.find_element_by_id('input_value')
    input2 = browser.find_element_by_id('answer')
    # print(input1)
    x = input1.text
    # print(x)
    y = calc(x)
    input2.send_keys(y)
    button2 = browser.find_element_by_css_selector("button.btn")
    button2.click()
finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()