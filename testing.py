import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


website = "https://fp.lmu.edu.ng"
path =r"\Users\Django\Downloads\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)


# get school login page 
driver.get(website)


# form interactions 
username = driver.find_element(by='xpath', value="//input[@id='username']")
password = driver.find_element(by='name', value= 'password')
login_btn = driver.find_element(by='xpath', value="//input[@type='submit']")


# User credentials 
username.send_keys('ekong.emmanuel')
password.send_keys('2020lmucom2020')
login_btn.click()
