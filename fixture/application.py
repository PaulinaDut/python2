from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:

    def _init_(self):
        self.driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver.exe")
        self.vars = {}

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def create_group(self, group):
        self.open_groups_page()
        # init group creation
        self.driver.find_element(By.NAME, "new").click()
        # fill group form
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(2)").click()
        # submit group creation
        self.driver.find_element(By.NAME, "submit").click()

    def open_groups_page(self):
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def login(self, username, password):
        self.open_home_page()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def open_home_page(self):
        self.driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver.exe")
        self.driver.get("http://localhost/")

    def destroy(self):
        self.driver.quit()