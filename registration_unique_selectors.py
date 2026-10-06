from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)

    input1 = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
    input3.send_keys("test@test.ru")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" in welcome_text
    print("TEST PASSED: registration1 - OK")

finally:
    time.sleep(10)
    browser.quit()


