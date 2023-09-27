import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service


driver = webdriver.Edge()
driver.get('https://fp.lmu.edu.ng/')
title = driver.title
print(title)
