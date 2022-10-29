from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://mail.google.com/")

elem = driver.find_element(By.NAME, "identifier")
elem.clear()
elem = driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()
elem.send_keys("dannyk3v@gmail.com")

elem = driver.find_element(By.NAME, "Passwd")
elem.clear()
elem = driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()
elem.send_keys("preethkev02")

elem = driver.find_element(By.CLASS_NAME, "gb_Ba gbii").click()
elem = driver.find_element(By.CLASS_NAME, "SedFmc").click()


sleep(10)
driver.close()