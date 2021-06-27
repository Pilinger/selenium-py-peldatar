# preparing selenium and chrome web driver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# importing os for running docker-compose up -d
import os

driver = webdriver.Chrome(ChromeDriverManager().install())

os.system('docker-compose up -d')

driver.get('http://localhost:9999/kitchensink.html')

# a tricky way to get ends-with 'radio',
# because browsers support xpath 1.0, and ends-with is xpath 2.0
cars = driver.find_elements_by_xpath("//*[substring(@id, string-length(@id) - string-length('check') +1) = 'check']")
# displaying the check's id
for item in cars:
    print(item.get_attribute('id'))
print()

# displaying the show-hide element's id
input = driver.find_element_by_xpath("//*[@name='show-hide']")
print(input.get_attribute('id'))
print()

# displaying the text of the legends
legends = driver.find_elements_by_xpath("//legend")
for legend in legends:
    print(legend.text)