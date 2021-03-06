# Generated by Selenium IDE
from selenium.webdriver.chrome.webdriver import WebDriver
import selenium.webdriver.common.by

def test_add_group():

    driver = WebDriver(executable_path="C:\selenium\chromedriver.exe")
    driver.get("http://localhost/")
    driver.find_element(selenium.webdriver.common.by.By.NAME, "user").send_keys("admin")
    driver.find_element(selenium.webdriver.common.by.By.NAME, "pass").send_keys("secret")
    driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR, "input:nth-child(7)").click()
    driver.find_element(selenium.webdriver.common.by.By.LINK_TEXT, "groups").click()
    driver.find_element(selenium.webdriver.common.by.By.NAME, "new").click()
    driver.find_element(selenium.webdriver.common.by.By.NAME, "group_name").click()
    driver.find_element(selenium.webdriver.common.by.By.NAME, "group_name").send_keys("test2")
    driver.find_element(selenium.webdriver.common.by.By.NAME, "submit").click()
    driver.find_element(selenium.webdriver.common.by.By.LINK_TEXT, "home").click()
    driver.find_element(selenium.webdriver.common.by.By.LINK_TEXT, "Logout").click()
  
