import time
import unittest
from selenium import webdriver

from logic.api_page import UserPage
from logic.cart_page import CartPage
from logic.home_page import HomePage
from logic.login_page import LoginPage
from infra.api_infra.api_wrapper import APIWrapper
from utils.api_get_data import AbiGetData
from infra.api_infra.api_test_base import APITestBase


class posTitleTest(APITestBase):

    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.firefox_options = webdriver.FirefoxOptions()
        # self.edge_options = webdriver.EdgeOptions()
        self.browsers_list = [self.chrome_options, self.firefox_options]
        # options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        # options.add_argument("--no-sandbox")  # This line is often necessary in CI environments
        # options.add_argument("--disable-dev-shm-usage")  # This can help in environments with limited resources
        self.my_api = APIWrapper()
        self.url_add_to_cart = "https://www.terminalx.com/pg/MutationAddAnyProductsToAnyCart"
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.terminalx.com/")
        self.get_data = AbiGetData(self.driver)

    def test_api_add_cart(self):
        results = self.my_api.api_post_request(self.url_add_to_cart, self.get_data.get_body_conf_add_item(),
                                               self.get_data.get_cookie_conf())
        print(results)
    # def test_parallel(self):
    #     with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browsers_list)) as executor:
    #         executor.map(self.test_check_card, self.browsers_list)

    def test_check_card(self):
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.home_page.click_login()
        self.login_page.login_flow()
        # self.my_api.api_post_request(self.url_add_to_cart, self.get_data.get_body_conf_add_item(),
        #                              self.get_data.get_cookie_conf())
        time.sleep(5)
        self.home_page.click_on_cart_button()
        self.home_page.click_go_to_card_button()
        self.assertTrue(self.cart_page.card_is_not_empty(), "card is not empty")


if __name__ == "__main__":
    unittest.main()
