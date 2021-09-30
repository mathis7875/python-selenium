import pytest
import allure

from locators.locators import LoginPage,MarketPlace,CashierPage
from pages.login_market_place import LoginMarketPlace
from pages.market_place_page import MarketPlacePage

@pytest.mark.usefixtures("setup")

class TestMarketPlaceMerchant:

    @allure.title("Login marketplace with and change ple")
    @allure.description("Login marketplace with and change ple")

    def test_marketplace_ple_test(self):
        open_market_page = MarketPlacePage(self.driver)
        open_market_page.open_page()
        merchant_store_login = LoginMarketPlace(self.driver)
        merchant_store_login.login_with_input("qa23us toxx", "nr9TypRH1b0B") 
        merchant_store_page =  MarketPlacePage(self.driver)
        merchant_store_page.click_my_account
        merchant_store_page.click_manage_subscriptions

    #add  ple
    #save
    #delete ple 
    #assert if create sub still show
    