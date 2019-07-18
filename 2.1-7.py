from selenium import  webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def print_answer(remote: webdriver.Remote):
  alert = remote.switch_to.alert
  print(alert.text.split()[-1])
  alert.accept()

url="http://suninjuly.github.io/get_attribute.html"
browser=webdriver.Chrome()
browser.get(url)

x_element = browser.find_element_by_id("treasure")
x=x_element.get_attribute("valuex")
browser.find_element_by_id("answer").send_keys(calc(x))

browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()

browser.find_element_by_css_selector("button[type=submit]").click()

print_answer(browser)
browser.quit()
