from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest


def expected(test1):
    webdriver.Chrome("C:\\Users\\HP\\Downloads\\chromedriver_win32\\chromedriver.exe")

    driver.get('http://google.com')

    driver.find_element(By.NAME, "q").send_keys("ferrrari").click()
    expected = string("displaying at least 10 search results")

def actual(test2):
     webdriver.Chrome("C:\\Users\\HP\\Downloads\\chromedriver_win32\\chromedriver.exe")


     driver.get('http://google.com')

     driver.find_element(By.CLASS_NAME, "OBMEnb")
     actual = string("displaying at least 10 search results")

assert expected(test1="displaying at least 10 search results") == actual(test2="displaying at least 10 search results")
