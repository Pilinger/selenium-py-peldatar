# preparing selenium and chrome webdriver manager
import selenium.common.exceptions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# opening the site
driver.get('http://www.pizzaparadicsom.hu/')

# capturing the ...NoSuchElementException error
try:
    none_id = driver.find_element_by_id("nemletezik")
except selenium.common.exceptions.NoSuchElementException:
    print('No such id as "nemletezik"')