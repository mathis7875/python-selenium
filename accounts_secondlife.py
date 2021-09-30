import logging
import allure
from selenium.webdriver.common.keys import Keys
from locators.locators import LoginPage,HomePage


class AccountsSecondlife:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)


    @allure.step("Opening secondlife.com website")
    def open_page(self):
       self.logger.info("Opening secondlife.com website")
       self.driver.get("https://secondlife.com/")

    @allure.step("Go to header ")
    def click_account_menu_header_with_welcome(self):
        self.logger.info("Go to welcome header")
        self.driver.find_element(*HomePage.accountmenubuttonByLink).click()
           