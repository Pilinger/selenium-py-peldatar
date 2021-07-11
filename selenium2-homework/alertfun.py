# preparing selenium and chrome web driver manager and time
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# importing ActionChains for doubleclick
from selenium.webdriver.common.action_chains import ActionChains

# importing os for running docker-compose up -d
import os


def invoke_alert(button, double, message):
    time.sleep(0.5)
    if double:
        action_chains = ActionChains(driver)
        action_chains.double_click(button).perform()
    else:
        button.click()
    alert = driver.switch_to.alert
    time.sleep(0.5)
    if message != '':
        time.sleep(2)
        '''
        The send_keys message does not appear in the prompt visually,
        but the alert gets the keys, and the paragraph displays it correctly.
        This switch to the current window not helped either
        using chrome driver.
        current_window = driver.window_handles[0]
        driver.switch_to.window(current_window)
        '''
        alert.send_keys(message)
        time.sleep(2)
    alert.accept()
    time.sleep(0.5)
    if message != '':
        assert(driver.find_element_by_id('demo').text == 'You entered: ' + message)


# initialising driver, starting the docker
driver = webdriver.Chrome(ChromeDriverManager().install())
os.system('docker-compose up -d')

try:
    #  opening the site
    driver.get('http://localhost:9999/alert_playground.html')
    # getting the needful buttons
    a_button = driver.find_element_by_name('alert')
    c_button = driver.find_element_by_name('confirmation')
    p_button = driver.find_element_by_name('prompt')
    d_button = driver.find_element_by_id('double-click')

    invoke_alert(a_button, False, '')
    invoke_alert(c_button, False, '')
    invoke_alert(p_button, False, 'This text should appear afterwards...')
    invoke_alert(d_button, True, '')
finally:
    time.sleep(1)
    driver.close()