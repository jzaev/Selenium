from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")
event = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

li_list = event.find_elements(By.TAG_NAME, "li")
res = {}

for i, li in enumerate(li_list):
    lines = li.text.split("\n")
    res[i] = {"time": "2023-"+lines[0], "name": lines[1]}
print(res)
