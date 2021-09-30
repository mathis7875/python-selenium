import pytest
import allure
from locators.locators import LoginPage, MarketPlace
from pages.login_market_place import LoginMarketPlace
from pages.market_place_page import MarketPlacePage


@pytest.mark.usefixtures("setup")
class TestLoginMarketPlace:

    @allure.title("Login marketplace with valid data test")
    @allure.description("This is test of marketplace login with valid data")
    def test_market_place_login(self):
        open_market_page = MarketPlacePage(self.driver)
        open_market_page.open_page()
        markeet_place_login = LoginMarketPlace(self.driver)     
        markeet_place_login.login_with_input("sl0m2", "ossmtester$")
        markeet_place_login.logout_marketplace()
        