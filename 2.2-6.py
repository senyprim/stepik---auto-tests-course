from selenium import  webdriver
import  math
def func(x):
    return math.log(abs(12*math.sin(x)))

def print_alert(handle:webdriver):
    alert=browser.switch_to.alert
    print(alert.text)
#    alert.accept()

def scrollToVisible(browser:webdriver,element):
    browser.execute_script("return arguments[0].scrollIntoView(true);",element)
    return element



browser=webdriver.Chrome()

browser.get("https://suninjuly.github.io/execute_script.html")

x=int(browser.find_element_by_id("input_value").text)
print(x)
print(str(func(x)))
browser.find_element_by_id("answer").send_keys(str(func(x)))

browser.find_element_by_id("robotCheckbox").click()
scrollToVisible(browser,browser.find_element_by_id("robotsRule")).click()

submit=browser.find_element_by_css_selector("button[type=submit]")
scrollToVisible(browser,submit).click()

print_alert(browser)
#browser.quit()