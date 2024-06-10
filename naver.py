from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyperclip

from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument(r'user-driver-dir=C:\Users\CKIRUser\AppData\Local\Google\Chrome\User Data\Profile 7')

driver = webdriver.Chrome(options=options)
driver.get('https://nid.naver.com/nidlogin.login?svctype=262144')

time.sleep(2)

pyperclip.copy('tjdals8642')

e = driver.find_element(By.CSS_SELECTOR, '#id')
e.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

pyperclip.copy('ckddnjsduwk1')

e = driver.find_element(By.CSS_SELECTOR, '#pw')
e.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

e.send_keys(Keys.ENTER)

time.sleep(1000000)
