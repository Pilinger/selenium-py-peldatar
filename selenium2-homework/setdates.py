# preparing selenium and chrome web driver manager
import time
import datetime

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# importing os for running docker-compose up -d
import os

driver = webdriver.Chrome(ChromeDriverManager().install())

os.system('docker-compose up -d')

driver.get('http://localhost:9999/forms.html')

# getting the input elements
date = driver.find_element_by_id('example-input-date')
date_time = driver.find_element_by_id('example-input-date-time')
date_time_local = driver.find_element_by_id('example-input-date-time-local')
month = driver.find_element_by_id('example-input-month')
week = driver.find_element_by_id('example-input-week')
timing = driver.find_element_by_id('example-input-time')

# clearing the inputs
date.clear()
date_time.clear()
date_time_local.clear()
month.clear()
week.clear()
timing.clear()

# fill out the date and time inputs
time.sleep(0.5)
d = datetime.datetime(2021, 6, 5)
date.send_keys(d.strftime('00%Y/%m/%d'))
time.sleep(0.5)
dt = datetime.datetime(2012, 5, 5, 5, 5, 5, 555)
date_time.send_keys(dt.strftime('%Y.%m.%d %H:%M:%S:%f'))
time.sleep(0.5)
dtl =  datetime.datetime(2000, 5, 12, 12, 1)
date_time_local.send_keys(dtl.strftime('00%Y.%m.%d%I%M'))
time.sleep(0.5)
m = datetime.datetime(1995, 12, 1)
month.send_keys(m.strftime('00%Y%B'))
time.sleep(0.5)
w = datetime.datetime(2015, 12, 31)
week.send_keys(w.strftime('%W00%Y'))
time.sleep(0.5)
t = datetime.datetime(2015, 12, 31, 12, 25)
timing.send_keys(t.strftime('%H%M%p'))
