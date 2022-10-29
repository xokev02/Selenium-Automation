from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from time import time
import json
#import unittest

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.amazon.in/")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")

driver.find_element(By.ID, "nav-link-accountList").click()

def signing_in ():
    with open('samples.json') as datafile:
        x = json.load(datafile)
        for x in datafile:   
        # For Email Or User Name...
            email = driver.find_element(By.ID, "ap_email")
            email.clear()
            email.send_keys(datafile[x].Email)
            driver.find_element(By.ID, "continue").click()
        # For Password
            password = driver.find_element(By.ID, "ap_password")
            password.clear()
            password.send_keys(datafile[x].Password)
            driver.find_element(By.ID, "signInSubmit").click()

            driver.quit()
            return 0

            # class amazon(unittest.TestCase):
#     def test_ing(self):
#         with open('testdata.csv') as data_file:    
#             data_file = csv.reader(data_file)
#             for line in data_file:
#                 self.driver = webdriver.Chrome()
#                 self.driver.maximize_window()
#                 self.driver.get("https://www.amazon.in/")
#                 signin= self.driver.find_element(By.ID, "nav-link-accountList").click()
#                 email = self.driver.find_element(By.ID, "ap_email")
#                 email.send_keys(line[0])
#                 contue = self.driver.find_element(By.ID, "continue").click()
#                 password=self.driver.find_element(By.ID, "ap_password")
#                 password.send_keys(line[1])
#                 sign_in=self.driver.find_element(By.ID, "signInSubmit").click()
#                 self.driver.quit()


signing_in()
