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
driver.implicitly_wait(10)

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
time.sleep(1)

# e = driver.find_element(By.CSS_SELECTOR, '#new.dontsave').click()
# time.sleep(2)

driver.get('https://m.blog.naver.com/FeedList.naver')
time.sleep(1.5)

driver.get('https://blog.editor.naver.com/editor?deviceType=mobile&returnUrl=https%3A%2F%2Fm.blog.naver.com%2FGoWriteForm.naver')
time.sleep(1.5)

e = driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="제목"]') #Better to be specific
e.send_keys('Testing')

e = driver.find_element(By.CSS_SELECTOR, 'div[placeholder="내용을 입력하세요."]') #Better to be specific
e.send_keys('Code\nIn progress')
e.send_keys(Keys.ENTER)
e.send_keys('hehe')
# publish
# e = driver.find_element(By.CSS_SELECTOR, 'editor-header .btn_applyPost').click()
time.sleep(1000000)

