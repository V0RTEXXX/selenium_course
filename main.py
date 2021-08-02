# 1) Проверьте, что можно зарегистрироваться на сайте, заполнив только обязательные поля, отмеченные символом *:
# First name, last name, email. Текст для полей может быть любым. Успешность регистрации проверяется сравнением
# ожидаемого текста "Congratulations! You have successfully registered!" с текстом на странице, которая открывается
# после регистрации. Для сравнения воспользуемся стандартной конструкцией assert из языка Python. Попробуйте

# 2) Запустить код из предыдущего шага, указав в качестве начальной страницы новую ссылку
# http://suninjuly.github.io/registration2.html. Если ваш тест упал с ошибкой NoSuchElementException, это означает,
# что вы выбрали правильные селекторы и смогли обнаружить баг, который создали разработчики. Это хорошо! Значит,
# ваши тесты сработали как надо.


from selenium import webdriver
import time

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/registration2.html"  # для успешного прохождения теста вставить ссылку
    # http://suninjuly.github.io/registration1.html

    browser.get(link)

    # Код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
    last_name.send_keys("Petrov")
    email = browser.find_element_by_css_selector('input[placeholder="Input your email"]')
    email.send_keys("qqq@mail.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()