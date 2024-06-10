from selenium import webdriver # type: ignore
from selenium.webdriver.common.keys import Keys  # type: ignore
import time
from selenium.webdriver.common.by import By
import urllib.request

# options = webdriver.ChromeOptions()
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
# options.add_argument('user-agent=' + user_agent)
driver = webdriver.Chrome()
driver.set_window_size(1600, 1920)
driver.get('https://instagram.com')
driver.implicitly_wait(10)

e = driver.find_element(By.CSS_SELECTOR,'input[name="username"]')
e.click()
e.send_keys('id') #Your account's ID
e = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
e.click()
e.send_keys('pw') #Your account's password
e.send_keys(Keys.ENTER)
time.sleep(2)

driver.get('https://instagram.com/explore/tags/먹거리/')
driver.implicitly_wait(10)

#click the first image
# time.sleep(2)
e = driver.find_element(By.CSS_SELECTOR, '._aagw').click()

#save the image
# time.sleep(2)

for i in range(10):
    try:
        image = driver.find_element(By.CSS_SELECTOR, '._aatb .x5yr21d').get_attribute('src')
        urllib.request.urlretrieve(image, f'{i}.jpg')
        # time.sleep(2)
    except:
        e = driver.find_element(By.CSS_SELECTOR, '._aaqg  ._abl-')
        driver.execute_script('arguments[0].click();', e)
        # time.sleep(2)
    # next image
    e = driver.find_element(By.CSS_SELECTOR, '._aaqg  ._abl-')
    driver.execute_script('arguments[0].click();', e)
    # time.sleep(2)

# time.sleep(1000000)