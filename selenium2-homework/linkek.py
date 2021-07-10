# preparing selenium and chrome web driver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# importing os for running docker-compose up -d
import os

driver = webdriver.Chrome(ChromeDriverManager().install())

os.system('docker-compose up -d')

driver.get('http://localhost:9999')

links = driver.find_elements_by_xpath('//a')

list_links = []
for link in links:
    list_links.append(link.get_attribute('href'))

with open('all_links.txt', 'w', encoding='utf-8') as all_links:
    all_links.write('\n'.join(list_links))
