from selenium import  webdriver
import math
import time

def print_alert(handle:webdriver):
    alert=handle.switch_to.alert
    print(alert.text)
    alert.accept

browser=webdriver.Chrome()
#Открыть 1 страницу
browser.get("http://suninjuly.github.io/redirect_accept.html")
#Нажать на кнопку
browser.find_element_by_css_selector("button[type=submit]").click()
#Перейти на новую вкладку
browser.switch_to.window(browser.window_handles[1])
#Считываем число
x=int(browser.find_element_by_id("input_value").text)
#Расчитываем результат
result=math.log(abs(12*math.sin(x)))
#Записываем результат
browser.find_element_by_id("answer").send_keys(str(result))
#Нажать submit
browser.find_element_by_css_selector("button[type=submit]").click()

#Напечатать конечный алерт
print_alert(browser)
browser.quit()





