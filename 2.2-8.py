from selenium import webdriver
import  os
import time

def print_alert(handle:webdriver):
    alert = handle.switch_to.alert
    print(alert.text)

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")
fields=["firstname","lastname","email"]
answ=["Иван","Иванов","ivanov@mail.ru"]
field_answ=dict(zip(fields,answ))

for fields,answ in field_answ.items():
    browser.find_element_by_name(fields).send_keys(answ)

filename=os.path.join(os.path.abspath(os.path.dirname(__file__)),"empty.txt")
browser.find_element_by_css_selector("input[type=file]").send_keys(filename)
time.sleep(1)
browser.find_element_by_css_selector("button[type=submit]").click()
print_alert(browser)


