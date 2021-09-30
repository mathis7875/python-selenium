import pytest
import allure

from locators.locators import LoginPage,MarketPlace,CashierPage
from pages.login_market_place import LoginMarketPlace
from pages.market_place_page import MarketPlacePage

@pytest.mark.usefixtures("setup")
class TestMarketPlaceShopping:

    @allure.title("Verify Search for merchant store slm01 tester")
    @allure.description("Verify Search for merchant store slm01 tester")
    def test_search_for_merchant_store(self):
        open_market_page = MarketPlacePage(self.driver)
        open_market_page.open_page()
        merchant_store_login = LoginMarketPlace(self.driver)
        merchant_store_login.login_with_input("qa23us toxx", "nr9TypRH1b0B")
        merchant_store_page =  MarketPlacePage(self.driver)
        merchant_store_page.search_merchant_store_tab("sl0m1")
       #merchant_store_page.search_merchant_store_by_keyword("sl0m1")
        search_result = "SLM01 Tester"
        assert search_result in self.driver.find_element(*MarketPlace.slm01_store).text
       
        #merchant_store_login.logout_marketplace()
    @allure.title("Verify Item Test Enter a safe And Check Results")
    @allure.description("Verify Item Test Enter a safe And Check Results")
    def test_marketplace_items_for_safe_key_word(self):
        open_market_page = MarketPlacePage(self.driver)
        open_market_page.open_page()
        merchant_store_login = LoginMarketPlace(self.driver)
        merchant_store_login.login_with_input("qa23us toxx", "nr9TypRH1b0B") #use GM userlogin
        merchant_store_page =  MarketPlacePage(self.driver)
        merchant_store_page.search_merchant_store_by_item_keyword("happy")

        search_result = "49232 matching items found"
        assert search_result in self.driver.find_element(*MarketPlace.item_search_results).text


    @allure.title("Verify Item Test Enter a Unsafe And Check Results")
    @allure.description("Verify Item Test Enter a Unsafe And Check Results")
    def test_marketplace_items_for_unsafe_key_word(self): 
        open_market_page = MarketPlacePage(self.driver)
        open_market_page.open_page()
        merchant_store_login = LoginMarketPlace(self.driver)
        merchant_store_login.login_with_input("SLMunder18new", "ossmtester$") #use GM no a userlogin
        merchant_store_page =  MarketPlacePage(self.driver)
        merchant_store_page.search_merchant_store_by_item_keyword("xxx")

        search_result = "xxx"
        assert search_result in self.driver.find_element(*MarketPlace.item_search_results).text


    @allure.title("Verify user can buy item with $L1")
    @allure.description("Verify user can buy item with $L1")    
    def test_marketplace_store_buy_gift_with_one_Liden_dollar(self):    
        open_market_page = MarketPlacePage(self.driver)
        open_market_page.open_page()
        merchant_store_login = LoginMarketPlace(self.driver)
        merchant_store_login.login_with_input("qa23us toxx", "nr9TypRH1b0B") #use GM userlogin
        merchant_store_page =  MarketPlacePage(self.driver)
        merchant_store_page =  MarketPlacePage(self.driver)
        merchant_store_page.search_merchant_store_by_item_keyword("!!BH Midevil fire place!!!")
        merchant_store_page.buy_store_item_with_liden_dollar_by_item_link("/p/BH-Midevil-fire-place/12136238")
        merchant_store_page.click_buy_now_on_cashier_page()#maybe move to cashier page

        search_result = "DeliverySuccessAlert"
        assert search_result in self.driver.find_element(*CashierPage.payment_successful).text


    @allure.title("Verify user can buy item with $L0")
    @allure.description("Verify user can buy item with $L0")    
    def test_marketplace_store_buy_gift_with_zero_Liden_dollar(self):    
        open_market_page = MarketPlacePage(self.driver)
        open_market_page.open_page()
        merchant_store_login = LoginMarketPlace(self.driver)
        merchant_store_login.login_with_input("qa23us toxx", "nr9TypRH1b0B") #use GM userlogin
        merchant_store_page =  MarketPlacePage(self.driver)
        merchant_store_page =  MarketPlacePage(self.driver)
        merchant_store_page.search_merchant_store_by_item_keyword("Country Couture Baby's Got Her Blue Jeans On Demo")
        merchant_store_page.buy_store_item_with_liden_dollar_by_item_link("/p/Country-Couture-Babys-Got-Her-Blue-Jeans-On-Demo/8805056")
        merchant_store_page.click_buy_now_on_cashier_page()#maybe move to cashier page

        flash_notice = "Click 'Place your order' at the bottom of the page to complete checkout"
        assert flash_notice in self.driver.find_element(*MarketPlace.place_your_order_notice).text

        merchant_store_page.click_place_your_order_bttn()
        merchant_store_page.click_buy_now_on_cashier_page()

        search_result = "DeliverySuccessAlert"
        assert search_result in self.driver.find_element(*CashierPage.payment_successful).text  
           