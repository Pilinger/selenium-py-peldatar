# preparing selenium and chrome web driver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# importing os for running docker-compose up -d
import os

driver = webdriver.Chrome(ChromeDriverManager().install())

os.system('docker-compose up -d')

driver.get('http://localhost:9999/todo.html')

# getting the spans which are 'done-false', so an active thing to do
todos = driver.find_elements_by_xpath("//span[@class='done-false']")

# printing the list of todos
print('The list of todos:')
print("\n".join(f'{todo.text}' for todo in todos))
