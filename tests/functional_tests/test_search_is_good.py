import unittest
from selenium import webdriver
from logic.brands_page import BrandsPage

from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.check_out_payment_page import Check_Out_Page


class searchTest(unittest.TestCase):

    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.terminalx.com/")
        self.url_add_to_cart = "https://www.terminalx.com/pg/MutationAddAnyProductsToAnyCart"
        self.login_page = LoginPage(self.driver)
        self.checkout_page = Check_Out_Page(self)

    # test case num 3
    def test_search_is_good(self):
        self.home_page = HomePage(self.driver)
        self.home_page.search_btn()
        self.home_page.search_text("nike")
        self.brands_page = BrandsPage(self.driver)
        self.assertTrue(self.brands_page.search_is_displayed(), "search is not good")

    def test_search_not_good_key(self):
        self.home_page = HomePage(self.driver)
        self.home_page.search_btn()
        self.home_page.search_text("@כלהצ")
        self.brands_page = BrandsPage(self.driver)
        self.assertTrue(self.brands_page.search_keys_failed_is_displayed(), "search is not good")

    def tearDown(self):
        self.driver.quit()
