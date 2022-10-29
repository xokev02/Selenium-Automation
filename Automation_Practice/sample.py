#import email
#import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
#import csv
from time import time
driver = webdriver.Chrome()
driver.maximize_window() 

driver.get("https://www.amazon.in/")

elem = driver.find_element(By.ID, "nav-link-accountList").click()
# Email or Username
emailField = driver.find_element(By.ID, "ap_email")
emailField.clear()
emailField.send_keys("6374014581")

elem = driver.find_element(By.ID, "continue").click()
# Password
passwrdField = driver.find_element(By.ID, "ap_password")
passwrdField.clear()
passwrdField.send_keys("6374014581")

elem = driver.find_element(By.ID, "signInSubmit").click()

elem = driver.find_element(By.ID, "nav-hamburger-menu").click()

elem = driver.find_element(By.CLASS_NAME, "hmenu-item").click()

sleep(15)
driver.close()