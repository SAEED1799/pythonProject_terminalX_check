import unittest
from selenium import webdriver

from logic.brands_page import BrandsPage
from logic.cart_page import CartPage
from logic.home_page import HomePage
from logic.login_page import LoginPage


class posTitleTest(unittest.TestCase):

    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.firefox_options = webdriver.FirefoxOptions()
        # self.edge_options = webdriver.EdgeOptions()
        self.browsers_list = [self.chrome_options, self.firefox_options]
        self.url_add_to_cart = "https://www.terminalx.com/pg/MutationAddAnyProductsToAnyCart"
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.terminalx.com/")

    # def test_parallel(self):
    #     with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browsers_list)) as executor:
    #         executor.map(self.test_check_card, self.browsers_list)

    # the test want to be one item at the card--i want to add item here
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
