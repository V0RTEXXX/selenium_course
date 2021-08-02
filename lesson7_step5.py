import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
  browser = webdriver.Chrome()
  browser.get(link)
  input1 = browser.find_element_by_id('input_value')
  input2 = browser.find_element_by_id('answer')
  # print(input1)
  x = input1.text
  # print(x)
  y = calc(x)
  input2.send_keys(y)
  checkbox1 = browser.find_element_by_id('robotCheckbox')
  checkbox1.click()
  radiobutton1 = browser.find_element_by_id('robotsRule')
  radiobutton1.click()
  button = browser.find_element_by_css_selector("button.btn")
  button.click()
finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()

