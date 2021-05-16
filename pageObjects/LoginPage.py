from selenium.webdriver.common.by import By


class LoginPage:
    txtbox_username = (By.ID, "Email")
    txtbox_password = (By.ID, "Password")
    btn_Login = (By.XPATH, "//button[text()='Log in']")
    link_logout_linktext = (By.LINK_TEXT, "Logout")

    def __init__(self, driver, username, password):
        self.driver = driver
        self.username = username
        self.password = password

    def Login(self):
        self.driver.find_element(*self.txtbox_username).clear()
        self.driver.find_element(*self.txtbox_username).send_keys(self.username)
        self.driver.find_element(*self.txtbox_password).clear()
        self.driver.find_element(*self.txtbox_password).send_keys(self.password)
        self.driver.find_element(*self.btn_Login).click()

    def clickLogout(self):
        self.driver.find_element(*self.link_logout_linktext).click()
