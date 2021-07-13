# preparing selenium and chrome web driver manager and time
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# importing os for running docker-compose up -d
import os


# clicking in and out to get empty field validates
# or sending 'invalid' string to get warning
def click_in_and_out(field, message):
    field.click()
    time.sleep(0.5)
    if field.get_attribute('id') == 'test-single-checkbox':
        field.click()
        time.sleep(0.5)
    if message != '':
        field.send_keys(message)
        time.sleep(0.5)


# asserting error messages
def asserting_error_messages(field, message):
    if field.get_attribute('id') == 'test-single-checkbox':  # id not changing
        assert (driver.find_element_by_id('single-checkbox-invalid').text == message)
    elif field.get_attribute('id') == 'test-terms-service':  # id not changing
        assert (driver.find_element_by_id('checkbox-invalid').text == message)
    else:  # otherwise get the parents parent and the div with the specified class
        assert (field.find_element_by_xpath('../../div[@class="validate-field-error-message"]').text == message)


# initialising driver, starting the docker
driver = webdriver.Chrome(ChromeDriverManager().install())
os.system('docker-compose up -d')

try:
    #  opening the site
    driver.get('http://localhost:9999/simplevalidation.html')
    # getting the needful fields, checkboxes
    email = driver.find_element_by_id('test-email')
    password = driver.find_element_by_id('test-password')
    conf_pass = driver.find_element_by_id('test-confirm-password')
    cust_num = driver.find_element_by_id('test-customer-number')
    dealer = driver.find_element_by_id('test-dealer-number')
    random = driver.find_element_by_id('test-random-field')
    date = driver.find_element_by_id('test-date-field')
    url = driver.find_element_by_id('test-url-field')
    r_text = driver.find_element_by_id('test-random-textarea')
    card_type = driver.find_element_by_id('test-card-type')
    card_num = driver.find_element_by_id('test-card-number')
    card_cvv = driver.find_element_by_id('test-card-cvv')
    exp_month = driver.find_element_by_id('test-card-month')
    exp_year = driver.find_element_by_id('test-card-year')
    s_check = driver.find_element_by_id('test-single-checkbox')
    terms = driver.find_element_by_id('test-terms-service')
    more = driver.find_element_by_id('test-terms-service-more')

    # checking the fields empty, and checkboxes unchecked, and 'invalid' strings
    click_in_and_out(email, '')
    click_in_and_out(password, '')
    click_in_and_out(conf_pass, '')
    click_in_and_out(cust_num, '')
    click_in_and_out(dealer, '')
    click_in_and_out(random, 'invalid')
    click_in_and_out(date, '')
    click_in_and_out(url, 'invalid')
    click_in_and_out(r_text, '')
    click_in_and_out(card_type, '')
    click_in_and_out(card_num, '')
    click_in_and_out(card_cvv, '')
    click_in_and_out(exp_month, '')
    click_in_and_out(exp_year, '')
    click_in_and_out(s_check, '')
    click_in_and_out(terms, '')

    # asserting error messages
    asserting_error_messages(email, 'Please enter an e-mail')
    asserting_error_messages(password, "This field can't be empty")
    asserting_error_messages(conf_pass, 'Please complete Desired Password')
    asserting_error_messages(cust_num, "This field can't be empty")
    asserting_error_messages(dealer, "This field can't be empty")
    asserting_error_messages(random, 'Should contain "twelve"')
    asserting_error_messages(date, "This field can't be empty")
    asserting_error_messages(url, 'Please enter a valid URL (starts with "http" or "https")')
    asserting_error_messages(r_text, "This field can't be empty")
    asserting_error_messages(card_type, 'Please select a card type')
    asserting_error_messages(card_num, 'Please enter a credit card number (no spaces)')
    asserting_error_messages(card_cvv, "This field can't be empty")
    asserting_error_messages(exp_month, 'Select a month')
    asserting_error_messages(exp_year, 'Select a year')
    asserting_error_messages(s_check, "This field can't be empty")
    asserting_error_messages(terms, 'Please agree to both to continue')
finally:
    time.sleep(1)
    driver.close()
