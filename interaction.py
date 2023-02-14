from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# chrome_driver_path = "C:\chromedriver\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# # stats = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# stats = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(stats.text)
#

chrome_driver_path = "C:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.appbrewery.co/p/newsletter")
e_mail = driver.find_element(By.NAME, "email")
e_mail.send_keys("Angela@repair.course\n")
# e_mail.send_keys(Keys.ENTER)
time.sleep(10)





