from selenium import webdriver                                      # Untuk mengimport webdriver nya
from selenium.webdriver.common.by import By                         # Untuk mempersingkat command aja, dan dipake untuk jadi indikator elemen
from selenium.webdriver.support.ui import WebDriverWait             # Untuk mempersingkat command aja, dan dipake untuk nunggu
from selenium.webdriver.support import expected_conditions as EC    # Untuk mempersingkat command aja, dan dipake untuk kondisi apapun yang expected
from selenium.common.exceptions import TimeoutException             # Untuk mempersingkat command aja, dan dipake untuk kondisi timeout
from selenium.common.exceptions import NoSuchElementException       # Untuk mempersingkat command aja, dan dipake untuk kondisi elemen ga kedeteksi
import webbrowser                                                   # Cuma untuk ngebuka link di browser default kalian
import os.path                                                      # Untuk ngecek aja, apakah suatu file / folder exist or not
import time

if(os.path.exists('./Credential.txt') == False):                    # Jika Credential.txt tidak ada (Maybe kehapus or what)
    os.system('python SetupEL.py')                                  # Maka system akan jalanin SetupEL.py dulu

f = open("Credential.txt", "r")                                     # Buka Credential.txt, baca file nya

usernameStr = f.readline()                                          # Baca 1st Line (Username nya)
passwordStr = f.readline()                                          # Baca 2nd Line (Password nya)

driver = webdriver.Chrome()                                         # Buka webdriver
driver.minimize_window()                                            # Minimize window nya
driver.get('https://myclass.apps.binus.ac.id/Auth')                 # Buka link tersebut

username = driver.find_element_by_id('Username')                    # Cari elemen dengan ID 'Username'
username.send_keys(usernameStr)                                     # Isi elemen tersebut dengan data dari variabel 'usernameStr'
password = driver.find_element_by_id('Password')                    # Cari elemen dengan ID 'Password'
password.send_keys(passwordStr)                                     # Isi elemen tersebut dengan data dari variabel 'passwordStr'

signInButton = driver.find_element_by_id('btnSubmit')               # Cari elemen dengan ID 'btnSubmit'
signInButton.click()                                                # Klik elemen tersebut

timeout = 20                                                        # Set timeout 20 detik sebagai batas waktu wait

try:
    WebDriverWait(driver, 
    timeout).until(EC.visibility_of_element_located((By.XPATH, 
    '//*[@id="studentViconList"]/tbody')))                          # Webdriver akan menunggu sampai elemen dengan XPath tersebut muncul

except TimeoutException:
    print("Timed out waiting for page to load")                     # Kalo ternyata setelah 20 detik kagak muncul" maka end program nya
    driver.quit()                                                   # Close semua (Browser and CMD)

for a in driver.find_elements_by_xpath('//a'):                      # Perulangan untuk semua //a di webpage
    links = a.get_attribute('href')                                 # Dapatkan isi 'href'

    ex1 = "https://myclass.apps.binus.ac.id/"                       # Pengecualian untuk link-link ini
    ex2 = None
    ex3 = "https://myclass.apps.binus.ac.id/Home/Index#"
    ex4 = "https://myclass.apps.binus.ac.id/Auth/Logout"
    ex5 = "https://twitter.com/binusmaya"
    ex6 = "http://facebook.com/universitas.bina.nusantara"

    if links != ex1 and links != ex2 and links != ex3 and links != ex4 and links != ex5 and links != ex6:
        webbrowser.open(links)                                      # Buka link paling atas
        break                                                       # Break program agar dia ga ngebuka link di bawahnya

f.close()                                                           # Kalo udah semuanya, close dokumen Credential.txt
driver.quit()                                                       # Dan close semua (Browser and CMD)