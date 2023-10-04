import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


website = "https://lmu.edu.ng/"
driver = webdriver.Chrome()

 

# get web page 
driver.get(website)

# web title 
title = driver.title

driver.implicitly_wait(0.5)

# Navbar 
navbar_container = driver.find_element(By.XPATH, '//div[@id="myNavbar"]')
navbar_container_ul = navbar_container.find_element(By.XPATH, './ul')
navbar_container_navlinks = navbar_container_ul.find_elements(By.XPATH, './li')

content_extracted =[]
for drop_down_links in navbar_container_navlinks:
    sub_links = drop_down_links.find_element(By.XPATH, './a')
   
    if sub_links.text == "RESEARCH":
        sub_links.click()
        navlinks_multi_column_dropdown = drop_down_links.find_elements(By.XPATH, './/ul[@class="multi-column-dropdown"]')
        
        for navlinks in navlinks_multi_column_dropdown:
            navlinks_link = navlinks.find_elements(By.XPATH, './li')

            for page_navlink in navlinks_link:
                a_tags = page_navlink.find_element(By.XPATH, './a')
                
                if a_tags.text == 'Repository':
                    window_name = a_tags.get_attribute("target")
                    a_tags.click()
                  
                    driver.switch_to.window(driver.window_handles[-1])
                    new_page_contents = driver.find_elements(By.XPATH, '//div[@class="ep_toolbox_content"]')

                    for new_page_content in new_page_contents:
                        content_title = new_page_content.find_element(By.XPATH, "./a").text
                        content_caption = new_page_content.text
                        content_extracted.append({"title":content_title, "caption":content_caption})

    else:
        pass     
                       
                    
print("Data extracted: ", content_extracted)                      
    

driver.quit()
