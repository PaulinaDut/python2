from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper
from fixture.group import GroupHelper



class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver.exe")
        self.vars = {}
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        self.driver.get("http://localhost/")

    def destroy(self):
        self.driver.quit()
