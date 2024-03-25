import unittest
from selenium import webdriver

from logic.cart_page import CartPage
from logic.home_page import HomePage
from logic.login_page import LoginPage
from infra.api_infra.api_wrapper import APIWrapper


class posTitleTest(unittest.TestCase):

    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.firefox_options = webdriver.FirefoxOptions()
        # self.edge_options = webdriver.EdgeOptions()
        self.browsers_list = [self.chrome_options, self.firefox_options]
        self.my_api = APIWrapper()
        self.url_add_to_cart = "https://www.terminalx.com/pg/MutationAddAnyProductsToAnyCart"
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.terminalx.com/")

    def api_add_cart(self):
        self.my_api.api_post_request(self.url_add_to_cart)

    # def test_parallel(self):
    #     with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browsers_list)) as executor:
    #         executor.map(self.test_check_card, self.browsers_list)

    #the test want to be one item at the card
    def test_check_remove_item(self):
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.home_page.click_login()
        self.login_page.login_flow()
        self.home_page.click_on_cart_button()
        self.home_page.click_go_to_card_button()
        self.cart_page.remove_item()
        self.assertTrue(self.cart_page.card_is_empty(), "card is empty")


if __name__ == "__main__":
    unittest.main()
