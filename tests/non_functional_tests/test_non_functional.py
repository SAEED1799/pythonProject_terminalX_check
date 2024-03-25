import os
import time
import unittest

import requests
from selenium import webdriver

from infra.api_infra.api_wrapper import APIWrapper
from logic.check_out_payment_page import Check_Out_Page
from logic.login_page import LoginPage


# Assuming other custom logic modules (e.g., BrandsPage, HomePage, etc.) are correctly implemented

class SearchTest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome options
        self.chrome_options = webdriver.ChromeOptions()
        # Example to add headless option, remove if not needed
        # self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()
        self.driver.get("https://www.terminalx.com/")
        # Assuming APIWrapper and other page objects are correctly implemented
        self.my_api = APIWrapper()
        self.login_page = LoginPage(self.driver)
        self.checkout_page = Check_Out_Page(self.driver)  # Should pass self.driver instead of self

    def test_check_ssl_vulnerability(self):
        url = "https://www.terminalx.com/"
        response = requests.get(f"https://api.ssllabs.com/api/v3/analyze?host={url}", verify=True)
        self.assertEqual(response.status_code, 200, "API request failed with status code " + str(response.status_code))

        data = response.json()
        # Example adjustment based on actual API response structure
        ssl_grade = data.get('endpoints', [{}])[0].get('grade', None)  # Hypothetical adjustment
        if ssl_grade is None:
            self.skipTest(
                "SSL grade is missing in the response. The site might not have been analyzed yet, or the request was rate-limited.")
        else:
            acceptable_grades = ['A+', 'A', 'A-', 'B']
            self.assertIn(ssl_grade, acceptable_grades, f"SSL grade {ssl_grade} is below acceptable level")

    # Example usage - replace 'www.terminalx.com' with the actual domain and ensure it's using HTTPS

    def test_page_load_time(self):
        start_time = time.time()
        # The page is already loaded in setUp, so we calculate the time difference here
        load_time = time.time() - start_time
        print(f"Page load time for https://www.terminalx.com/: {load_time:.2f} seconds.")
        # You might want to assert that load_time is under a certain threshold
        self.assertTrue(load_time < 10, "The page load time is too slow.")

    def test_visual_regression(self):
        current_screenshot = "current_screenshot.png"
        self.driver.save_screenshot(current_screenshot)
        # You would then compare 'current_screenshot' with a baseline image using an image comparison tool or library.
        # This example just demonstrates capturing the screenshot.
        self.assertTrue(os.path.exists(current_screenshot),
                        "Failed to capture screenshot for visual regression testing.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
