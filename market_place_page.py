import logging
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.locators import MarketPlace,CashierPage,MerchantHome

class MarketPlacePage:

 def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

 @allure.step("Opening marketplace.secondlife.com website")
 def open_page(self):
        self.logger.info("Opening marketplace.secondlife.com website")
        #self.driver.get("https://marketplace.secondlife-staging.com/")
        self.driver.get("https://marketplace.secondlife.com/")

 @allure.step("Opening merchant tab")
 def search_merchant_store_tab(self, merchantname): 
        self.logger.info("Opening merchant tab")
        self.driver.find_element(*MarketPlace.search_merchant_store_Tab).click()
        self.driver.find_element(*MarketPlace.search_merchant_by_keyword).send_keys(merchantname) 
        self.driver.find_element(*MarketPlace.merchant_search_button).click()

 @allure.step("Search merchant store")
 def search_merchant_store_by_keyword(self, keyword):
        self.logger.info("search merchant by key word")
        self.driver.find_element(*MarketPlace.search_merchant_by_keyword).send_keys(keyword)
        self.driver.find_element(*MarketPlace.merchant_search_button).click()     


 @allure.step("Search merchant store by item")
 def search_merchant_store_by_item_keyword(self, item_keyword):     
        self.logger.info("Search merchant store by item") 
        self.driver.find_element(*MarketPlace.item_keywords).send_keys(item_keyword) 
        self.driver.find_element(*MarketPlace.product_search_bttn).click()

 @allure.step("Buy item from market with liden dollar")
 def buy_store_item_with_liden_dollar_by_item_link(self, linked_text):
        self.logger.info("buy item for one liden dollar") 
        self.driver.find_element_by_link_text(linked_text).click()
        self.driver.find_element(*MarketPlace.buy_now_bttn).click()



 @allure.step("Click buy now on cashier page")
 def click_buy_now_on_cashier_page(self):
        self.logger.info("click buy now on cashier page")
        self.driver.find_element(*CashierPage.buy_now_bttn).click() 

 @allure.step("Click place your order")
 def click_place_your_order_bttn(self): 
        self.logger.info("Click place your order")
        self.driver.find_element(*MarketPlace.place_your_order_bttn).click()    

 @allure.step("Click my account")
 def click_my_account(self):
        self.logger.info("Click my account")
        self.driver.find_element(*MarketPlace.merchant_home).click()

 @allure.step("Click on manage subscriptions")
 def click_manage_subscriptions(self):
        self.logger.info("Click on manage subscriptions")
        self.driver.find_element(*MerchantHome.manage_subscriptions).click()
