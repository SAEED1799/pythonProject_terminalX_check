import time
import unittest
from selenium import webdriver
from logic.home_page import HomePage
from logic.login_page import LoginPage


class TerminalXLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.terminalx.com/")

    def test_login_to_terminal(self):
        self.home_page = HomePage(self.driver)
        self.home_page.click_login()
        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow()
        time.sleep(4)
        self.assertTrue(self.login_page.login_page_displayed(), "you sign in")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
