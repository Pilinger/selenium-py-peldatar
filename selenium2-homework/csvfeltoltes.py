# preparing selenium and chrome web driver manager
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# importing os for running docker-compose up -d
import os
# importing csv for csv file operation
import csv


def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


def fill_in(name, email, dob, phone):  # to fulfill the form
    # clearing the fields
    i_name.clear()
    i_email.clear()
    i_dob.clear()
    i_phone.clear()
    time.sleep(0.5)

    # fulfill the inputs
    i_name.send_keys(name)
    i_email.send_keys(email)
    i_dob.send_keys(dob)
    i_phone.send_keys(phone)
    time.sleep(0.5)

    # submit the data
    b_submit.click()


driver = webdriver.Chrome(ChromeDriverManager().install())

os.system('docker-compose up -d')

driver.get('http://localhost:9999/another_form.html')

# getting the input and button elements
i_name = driver.find_element_by_id('fullname')
i_email = driver.find_element_by_id('email')
i_dob = driver.find_element_by_id('dob')
i_phone = driver.find_element_by_id('phone')
b_submit = driver.find_element_by_id('submit')
b_export = driver.find_element_by_xpath('//button')

with open('table_in.csv', 'r', encoding='utf-8') as full_csv:  # opening the file for reading
    csv_reader = csv.reader(full_csv, delimiter=',')
    next(csv_reader)  # avoiding field names
    # calling fill_in function for each row in the file passing the fields
    for row in csv_reader:
        fill_in(row[0], row[1], row[2], row[3])
    # exporting the data to a csv file
    b_export.click()
    time.sleep(4)

# reopening the csv file just for sure, for avoiding the previous next function
with open('table_in.csv', 'r', encoding='utf-8') as full_csv:  # opening the file for reading
    csv_reader = csv.reader(full_csv, delimiter=',')
    # opening the table.csv for comparing
    with open(get_download_path() + '\\table.csv', 'r', encoding='utf-8') as output_csv:
        csv_compare = csv.reader(output_csv, delimiter=',')
        for row in csv_reader:
            row_comp = next(csv_compare)
            assert (row == row_comp)
