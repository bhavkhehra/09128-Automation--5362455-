from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import pytest


def test():
   driver = webdriver.Chrome("C:\\Users\\HP\\Downloads\\chromedriver_win32\\chromedriver.exe")

   driver.get('http://google.com')
   driver.find_element(By.NAME, "q").send_keys("ferrrari")
   expected = "displaying at least 10 search results"

   actual = "displaying at least 8 search results"

   assert expected != actual
