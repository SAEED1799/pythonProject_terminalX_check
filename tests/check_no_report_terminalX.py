import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TerminalXTest(unittest.TestCase):

    def setUp(self):
        # Initialize WebDriver (in this case, Chrome)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # Maximize the browser window

    def on_sale_is_displayed(self):
        time.sleep(5)
        try:
            package_title = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='app-root']/div[2]"
                                                            "/main/div[2]/div/div[1]/div/h1"))
            )
            return package_title.is_displayed()
        except TimeoutException:
            print("Timed out waiting for package title element to be visible")
            return False

    def test_terminal_x(self):
        self.driver.get("https://www.terminalx.com/")
        try:
            rentCar_button = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='app-root']/div[2]/"
                                                            "header/div/div[4]/nav/ul/li[4]/a"))
            )
            rentCar_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

        self.assertTrue(self.on_sale_is_displayed(), "on sale page ok")

    def tearDown(self):
        # Close the browser
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
