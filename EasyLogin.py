from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import webbrowser
import os.path

if(os.path.exists('./Credential.txt') == False):
    os.system('python SetupEL.py')

f = open("Credential.txt", "r")

usernameStr = f.readline()
passwordStr = f.readline()

driver = webdriver.Chrome()
driver.minimize_window()
driver.get('https://myclass.apps.binus.ac.id/Auth')

username = driver.find_element_by_id('Username')
username.send_keys(usernameStr)
password = driver.find_element_by_id('Password')
password.send_keys(passwordStr)

signInButton = driver.find_element_by_id('btnSubmit')
signInButton.click()

timeout = 20

try:
    WebDriverWait(driver, 
    timeout).until(EC.visibility_of_element_located((By.XPATH, 
    '//*[@id="studentViconList"]/tbody')))

except TimeoutException:
    print("Timed out waiting for page to load")
    driver.quit()

driver.implicitly_wait(5)
webbrowser.open(driver.find_element_by_xpath('//*[@id="studentViconList"]/tbody/tr[3]/td[12]/div/a').get_attribute('href'))
f.close()
driver.quit()
