from selenium import  webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

url="http://suninjuly.github.io/get_attribute.html"
browser=webdriver.Chrome()
browser.get(url)

x_element = browser.find_element_by_id("input_value")

browser.find_element_by_id("answer").send_keys(calc(x_element.text))
browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()

browser.find_element_by_css_selector("button[type=submit]").click()




