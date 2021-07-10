# preparing selenium and chrome web driver manager
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# importing os for running docker-compose up -d
import os

# needed for sending Ctrl+Backspace for Search... input to get back the full table
from selenium.webdriver.common.keys import Keys

def fill_in(name, price, quantity, category):
    # adding a new line and filling out the row
    button.click()
    time.sleep(0.5)
    tr_s = driver.find_elements_by_xpath('//tr')
    row = tr_s[-1]  # getting the last row added
    cells = row.find_elements_by_tag_name('td')
    cells[0].find_element_by_tag_name('input').send_keys(name)
    time.sleep(0.5)
    cells[1].find_element_by_tag_name('input').send_keys(price)
    time.sleep(0.5)
    cells[2].find_element_by_tag_name('input').clear()
    cells[2].find_element_by_tag_name('input').send_keys(quantity)
    time.sleep(0.5)
    cells[3].find_element_by_tag_name('input').send_keys(category)
    time.sleep(0.5)


driver = webdriver.Chrome(ChromeDriverManager().install())

os.system('docker-compose up -d')

driver.get('http://localhost:9999/editable-table.html')

# getting the button
button = driver.find_element_by_xpath('//button')

# getting starting rows
start_rows = len(driver.find_elements_by_xpath('//tbody/tr'))

# starting the fill_in function
fill_in('Set Item', '1000000', '1', 'Artifact')

# starting the fill_in function second time
fill_in('Temple', '10000000', '1', 'Fortress')

# getting the total rowcount after adding
added_rows = len(driver.find_elements_by_xpath('//tbody/tr'))

# a) rows were correctly added
assert (start_rows + 2 == added_rows)

# continuing with the Search...
search = driver.find_element_by_xpath('//div/div/div/input')
time.sleep(0.5)
search.send_keys('Set Item')
tr = driver.find_elements_by_xpath('//tr')
rows = tr[-1]  # getting the last row added
cell = rows.find_elements_by_tag_name('td')

# b) checking the Search...
assert (cell[0].find_element_by_tag_name('input').get_attribute('value') == 'Set Item')

# continuing with full table, needed to send_keys with Ctrl+a and delete
time.sleep(0.5)
search.send_keys(Keys.CONTROL + 'a')
time.sleep(0.5)
search.send_keys(Keys.DELETE)
