from pages.accounts_secondlife import AccountsSecondlife
import pytest
import allure
from locators.locators import LoginPage, MarketPlace,HomePage
from pages.login_market_place import LoginMarketPlace
from pages.login_secondlife import LoginPageSecondLife
from pages.market_place_page import MarketPlacePage

@pytest.mark.usefixtures("setup")
class TestAccountsHistoryPage:

    #Validate Welcome header
    @allure.title("Login SL and validate welcome header")
    @allure.description("This is test is to check the wlecome header info")
    def test_market_place_login(self):
        open_market_page = AccountsSecondlife(self.driver)
        open_market_page.open_page()
        second_life_login = LoginPageSecondLife(self.driver)     
        second_life_login.login_with_input("sl0m2", "ossmtester$")

        search_result = "Johngalt Linden"
        assert search_result in self.driver.find_element(*HomePage.accountlinkByText.text)
       
        
    #Validate Footer Linden Lab
    @allure.title("Login SL and validate linden lab header")
    @allure.description("This is test is to check the linden lab header info")
    def test_footer_header_lindenlab(self):
        open_home_page = AccountsSecondlife(self.driver)
        open_home_page.open_page()
        second_life_login = LoginPageSecondLife(self.driver)     
        second_life_login.login_with_input("sl0m2", "ossmtester$")

        search_result = "Linden Lab"
        assert search_result in self.driver.find_element(*HomePage.lindenlabheaderByText.text)
        

    #VAlidate Foooter Tilia
    @allure.title("Login SL and validate Tiliia header")
    @allure.description("This is test is to check the Tilia header info")
    def test_footer_header_lindenlab(self):
        open_home_page = AccountsSecondlife(self.driver)
        open_home_page.open_page()
        second_life_login = LoginPageSecondLife(self.driver)     
        second_life_login.login_with_input("sl0m2", "ossmtester$")

        search_result = "Tilia"
        assert search_result in self.driver.find_element(*HomePage.tiliaheaderByText.text)
  

    #Validate footer Second life 
    @allure.title("Login SL and validate second life header")
    @allure.description("This is test is to check the sl header info")
    def test_footer_header_lindenlab(self):
        open_home_page = AccountsSecondlife(self.driver)
        open_home_page.open_page()
        second_life_login = LoginPageSecondLife(self.driver)     
        second_life_login.login_with_input("sl0m2", "ossmtester$")

        search_result = "Second Life"
        assert search_result in self.driver.find_element(*HomePage.secondlifeheaderByText.text)
        

    #Validate Footer Connect with us      
    @allure.title("Login SL and validate connect with us  header")
    @allure.description("This is test is to check the connect with us header info")
    def test_footer_header_lindenlab(self):
        open_home_page = AccountsSecondlife(self.driver)
        open_home_page.open_page()
        second_life_login = LoginPageSecondLife(self.driver)     
        second_life_login.login_with_input("sl0m2", "ossmtester$")

        search_result = "Connect With Us"
        assert search_result in self.driver.find_element(*HomePage.connectwithusheaderByText.text)
        

    #validate footer Partner with us 
    @allure.title("Login SL and validate partner with us  header")
    @allure.description("This is test is to check the partner with us header info")
    def test_footer_header_lindenlab(self):
        open_home_page = AccountsSecondlife(self.driver)
        open_home_page.open_page()
        second_life_login = LoginPageSecondLife(self.driver)     
        second_life_login.login_with_input("sl0m2", "ossmtester$")
     

        search_result = "Partner With Us"
        assert search_result in self.driver.find_element(*HomePage.partnerwithusheaderByText.text)
        

  #validate left menu  account statements link 
    @allure.title("Login SL and validate partner with us  header")
    @allure.description("This is test is to check the partner with us header info")
    def test_footer_header_lindenlab(self):
        open_home_page = AccountsSecondlife(self.driver)
        open_home_page.open_page()
        second_life_login = LoginPageSecondLife(self.driver)     
        second_life_login.login_with_input("sl0m2", "ossmtester$")
        open_home_page.click_account_menu_header_with_welcome()

        search_result = "Partner With Us"
        assert search_result in self.driver.find_element(*HomePage.accountlinkByText.text)
     

    #TODO fix xpath and links 
    #validate left menu statements link 