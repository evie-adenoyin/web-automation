import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path=r'C:\Users\Django\Downloads\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service = service)
driver.implicitly_wait(4)

# get school login page 
driver.get("https://fp.lmu.edu.ng")


# form interactions 
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
login_btn = driver.find_element(By.CLASS_NAME, 'button')


# User credentials 
username.send_keys('ekong.emmanuel')
password.send_keys('password')
login_btn.click()

# Receipt print out 
trans_payment_receipt= driver.find_elements(By.CLASS_NAME,'trans_payment_receipt')[0]
trans_payment_receipt.click()

# profile interactions 
menulist_ul = driver.find_element(By.ID, 'menulist_ul')
dropdown_list = menulist_ul.find_elements(By.TAG_NAME, 'li')[2]
print(dropdown_list.text)
item_list = dropdown_list.find_element(By.TAG_NAME,'a')


# dropdown_list = driver.find_elements(By.CLASS_NAME, 'dropdown-toggle')[2]
# dropdown_list.click()
# dropdown_menu = driver.find_elements(By.CLASS_NAME,'dropdown-menu')[1]
# dropdown_menu.click()
