# preparing selenium and chrome web driver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# importing os for running docker-compose up -d
import os

driver = webdriver.Chrome(ChromeDriverManager().install())

os.system('docker-compose up -d')

driver.get('http://localhost:9999/trickyelements.html')

# gathering all the elements having an id
items = driver.find_elements_by_xpath('//*[@id]')

# iterating through the items and clicking the first button, then exit the loop
for item in items:
    if item.tag_name == 'button':
        item.click()
        label = driver.find_element_by_id('result').text
        btn_str = item.text + ' was clicked'
        assert(label == btn_str)
        break
