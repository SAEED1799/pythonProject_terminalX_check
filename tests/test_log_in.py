import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TerminalXLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
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

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
