from selenium.webdriver.common.by import By

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        self.app.driver.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        self.open_groups_page()
        # init group creation
        self.app.driver.find_element(By.NAME, "new").click()
        # fill group form
        self.app.driver.find_element(By.NAME, "group_name").click()
        self.app.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.app.driver.find_element(By.CSS_SELECTOR, "form:nth-child(2)").click()
        # submit group creation
        self.app.driver.find_element(By.NAME, "submit").click()