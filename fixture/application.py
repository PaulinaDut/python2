from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper



class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver.exe")
        self.vars = {}
        self.session = SessionHelper(self)

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


    def open_home_page(self):
        self.driver.get("http://localhost/")

    def destroy(self):
        self.driver.quit()
