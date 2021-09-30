import logging
import allure
from selenium.webdriver.common.keys import Keys
from locators.locators import LoginPage


class LoginMarketPlace:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    #methods for login 
    @allure.step("Opening secondlife.com website")
    def open_page(self):
        self.logger.info("Opening secondlife.com website")
        self.driver.get("https://marketplace.secondlife-staging.com/")


    @allure.step("Opening login page")
    def open_login_page(self):
        self.logger.info("Opening login page")
        self.driver.find_element(*LoginPage.usernameById).click()
        self.driver.find_element(*LoginPage.passwordById).click()
        self.driver.find_element(*LoginPage.submitByName).click()

    @allure.step("login with manual input")
    def login_with_input(self, username, password):
        self.logger.info("login with manual input")
        self.driver.find_element(*LoginPage.login_link).click()
        self.driver.find_element(*LoginPage.usernameById).send_keys(username)
        self.driver.find_element(*LoginPage.passwordById).send_keys(password)
        self.driver.find_element(*LoginPage.submitByName).click()

    @allure.step("log out")
    def logout_marketplace(self):
       self.driver.find_element(*LoginPage.logout).click()