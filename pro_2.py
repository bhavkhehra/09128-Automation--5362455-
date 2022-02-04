from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest


def expected():
    webdriver.Chrome("C:\\Users\\HP\\Downloads\\chromedriver_win32\\chromedriver.exe")

    driver.get('http://youtube.com')

    driver.find_element(By.CLASS_NAME, "search_query").send_keys("carry").click()

    expected = string("displaying at least 5 search results")


def actual():
    webdriver.Chrome("C:\\Users\\HP\\Downloads\\chromedriver_win32\\chromedriver.exe")

    driver.get('http://youtube.com')

    driver.find_element(By.CLASS_NAME, "sbsb_b")
    actual = string("displaying at least 5 search results")


assert actual() == expected()
