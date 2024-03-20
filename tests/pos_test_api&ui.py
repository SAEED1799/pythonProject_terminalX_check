import concurrent.futures
import time
import unittest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.api_wrapper import APIWrapper


class posTitleTest(unittest.TestCase):

    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.firefox_options = webdriver.FirefoxOptions()
        # self.edge_options = webdriver.EdgeOptions()
        self.browsers_list = [self.chrome_options, self.firefox_options]
        self.my_api = APIWrapper()
        self.url = "https://www.terminalx.com/pg/MutationAddAnyProductsToAnyCart"
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.terminalx.com/")

    def test_login_to_terminal_x(self):
        # Wait for the Login button to be clickable
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='app-root']/div[2]/header/div/div[2]/div[1]"))
        )

        # Click on the Login button
        login_button.click()

        # Wait for the login modal to appear
        time.sleep(2)

        # Enter valid credentials
        username_field = self.driver.find_element(By.XPATH, "//*[@id='panel-root']/div/div[3]/div/div/div/div[3]/div["
                                                            "1]/div/form/div[1]/div/input")
        password_field = self.driver.find_element(By.XPATH, "//*[@id='panel-root']/div/div[3]/div/div/div/div[3]/div["
                                                            "1]/div/form/div[2]/div/input")
        submit_button = self.driver.find_element(By.XPATH, "//*[@id='panel-root']/div/div[3]/div/div/div/div[3]/div["
                                                           "1]/div/form/div[3]/button")

        username_field.send_keys("saeed.esawi99@gmail.com")  # Replace 'your_username' with actual username
        password_field.send_keys("Saeed@1234")  # Replace 'your_password' with actual password

        # Submit the login form
        submit_button.click()

        # Wait for the page to load after login
        time.sleep(5)

    def card_is_not_empty(self):
        time.sleep(5)
        try:
            package_title = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='app-root']/div[2]/main"
                                                            "/div[2]/div/div/div[2]/div[1]/div[2]"))
            )
            return package_title.is_displayed()
        except TimeoutException:
            print("Timed out waiting for package title element to be visible")
            return False

    def test_api_add_cart(self):
        self.my_api.api_post_request(self.url)

    def test_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browsers_list)) as executor:
            executor.map(self.test_check_card, self.browsers_list)

    def test_check_card(self):

        self.test_login_to_terminal_x()
        self.my_api.api_post_request(self.url)
        #click on cart
        try:
            card_button = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='app-root']/div[2]/header/div"
                                                            "/div[2]/div[3]/div/a[2]"))
            )
            card_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")
        # click on see the card
        try:
            card_button = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='top-portal-root']/div[2]/div/div/div[3]/a[2]"))
            )
            card_button.click()
            time.sleep(5)
        except Exception as e:
            print(f"An error occurred: {e}")

        self.assertTrue(self.card_is_not_empty(), "card is not empty")


if __name__ == "__main__":
    unittest.main()
