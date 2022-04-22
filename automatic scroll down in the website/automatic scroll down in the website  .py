from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 


driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("https://www.facebook.com/lexfridman")

while driver.find_element_by_tag_name('div'):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    Divs=driver.find_element_by_tag_name('div').text
    
    if 0xFF == ord('q'):
        break
    