from selenium import webdriver
from selenium.webdriver.support.ui import Select

def print_alert(handle:webdriver):
    alert=handle.switch_to.alert
    print(alert.text)
#    alert.accept()

browser=webdriver.Chrome()

browser.get("http://suninjuly.github.io/selects2.html")

select=Select(browser.find_element_by_id("dropdown"))

val=(int(browser.find_element_by_id("num1").text)+
    int(browser.find_element_by_id("num2").text))

select.select_by_visible_text(str(val))

browser.find_element_by_css_selector("button[type=submit]").click()

print_alert(browser)
#browser.quit()