import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomer:
    # Add customer Page
    lnkCustomers_menu = (By.XPATH, "//a[@href='#']//p[contains(text(),'Customers')]")
    lnkCustomers_menuitem = (By.XPATH, "//span[@class='menu-item-title'][contains(text(),'Customers')]")
    btnAddnew = (By.XPATH, "//a[@class='btn bg-blue']")
    txtEmail = (By.XPATH, "//input[@id='Email']")
    txtPassword = (By.XPATH, "//input[@id='Password']")
    txtcustomerRoles = (By.XPATH, "//div[@class='k-multiselect-wrap k-floatwrap']")
    lstitemAdministrators = (By.XPATH, "//li[contains(text(),'Administrators')]")
    lstitemRegistered = (By.XPATH, "//li[contains(text(),'Registered')]")
    lstitemGuests = (By.XPATH, "//li[contains(text(),'Guests')]")
    lstitemVendors = (By.XPATH, "//li[contains(text(),'Vendors')]")
    drpmgrOfVendor = (By.XPATH, "//*[@id='VendorId']")
    rdMaleGender = (By.ID, "Gender_Male")
    rdFeMaleGender = (By.ID, "Gender_Female")
    txtFirstName = (By.XPATH, "//input[@id='FirstName']")
    txtLastName = (By.XPATH, "//input[@id='LastName']")
    txtDob = (By.XPATH, "//input[@id='DateOfBirth']")
    txtCompanyName = (By.XPATH, "//input[@id='Company']")
    txtAdminContent = (By.XPATH, "//textarea[@id='AdminComment']")
    btnSave = (By.XPATH, "//button[@name='save']")

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(*self.lnkCustomers_menu).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(*self.lnkCustomers_menuitem).click()

    def clickOnAddnew(self):
        self.driver.find_element(*self.btnAddnew).click()

    def setEmail(self, email):
        self.driver.find_element(*self.txtEmail).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(*self.txtPassword).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element(*self.txtcustomerRoles).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(*self.lstitemRegistered)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(*self.lstitemAdministrators)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element(*"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(*self.lstitemGuests)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(*self.lstitemRegistered)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(*self.lstitemVendors)
        else:
            self.listitem = self.driver.find_element(*self.lstitemGuests)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(*self.drpmgrOfVendor))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(*self.rdMaleGender).click()
        elif gender == 'Female':
            self.driver.find_element(*self.rdFeMaleGender).click()
        else:
            self.driver.find_element(*self.rdMaleGender).click()

    def setFirstName(self, fname):
        self.driver.find_element(*self.txtFirstName).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(*self.txtLastName).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(*self.txtDob).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(*self.txtCompanyName).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(*self.txtAdminContent).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(*self.btnSave).click()
