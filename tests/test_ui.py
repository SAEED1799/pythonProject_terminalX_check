import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.api_wrapper import APIWrapper


class TerminalXTest(unittest.TestCase):

    def setUp(self):
        # Initialize WebDriver (in this case, Chrome)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # Maximize the browser window
        self.my_api = APIWrapper()
        self.url = "https://www.terminalx.com/pg/MutationAddAnyProductsToAnyCart"

        self.driver.refresh()  # Refresh the page to apply the cookie

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

    def test_terminal_x(self):
        # Set the desired cookie with the correct domain
        self.driver.get("https://www.terminalx.com/")  # Navigate to the website to set the cookie
        self.driver.add_cookie(
            {
                'name': 'syte_uuid',
                'value': '8aec36f0-e1e9-11ee-91fa-ab30a63932d8',
                'domain': '.terminalx.com',
                '_gcl_au': '1.1.1432958371.1710410368',
                'PHPSESSID': 'b66l8hriiu0ebo2eshib867448',
                '_fbp': 'fb.1.1710410368098.1603310446',
                '_tt_enable_cookie': '1',
                '_ttp': 'm8Q9hhUkfDKHM8NhnD7sXmYXewC',
                'glassix-visitor-id-v2-b6d2bc1d-dcdc-4766-b620-28559157075a': 'ab845d32-8366-419f-b392-301556435cb0',
                'fe-version': '7b110f0660db1bb8ab526e088cc9148d2e3ddc3a',
                'language': 'he',
                'wz.uid': 'q17SBw8Il61I267G510C17u58',
                'current-universe-id-1': '67',
                'syte_ab_tests': '{}',
                '_gid': 'GA1.2.1711495902.1710835220',
                '_ga': 'GA1.1.539162828.1710410367',
                '_uetsid': 'bbc9c2d0e5c611eeae02e7e838525cb6',
                '_uetvid': '8b8fa710e1e911ee878375296a5e3c47',
                'RSESSIONID': 'a5e55654-e18e-463f-8cec-5e78e3d884b2',
                'stimgs': '{"sessionId":10977087,"didReportCameraImpression":false,"newUser":null}',
                'slider_animation': '1',
                'wz_visited_pages': '{"counter":14}',
                '_dc_gtm_UA-99383422-1': '1',
                'private_content_version': '2309a3e235169b0b27cd0c330845479f',
                '_ga_Z2CGV88685': 'GS1.1.1710838210.5.1.1710839948.0.0.0'
            }

        )
        # Add more cookies similarly for other values...

        self.driver.refresh()  # Refresh the page to apply the cookie

        # Navigate to Terminal X website
        self.driver.get("https://www.terminalx.com/")
        try:
            cart_button = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[@id='app-root']/div[2]/header/div/div[2]/div[3]/div/a[2]"))
            )
            cart_button.click()
            time.sleep(5)
        except Exception as e:
            print(f"An error occurred: {e}")

            # click on see the card
            try:
                card_button = WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "// *[ @ id = 'top-portal-root']"
                                                                " / div[1] / div / div / div[3] / a[2]"))
                )
                card_button.click()
            except Exception as e:
                print(f"An error occurred: {e}")

        self.assertFalse(self.card_is_not_empty(), "card is not empty")

    def tearDown(self):
        # Close the browser
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# import concurrent.futures
# import time
# import unittest
# from selenium import webdriver
# from selenium.common import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# from infra.api_wrapper import APIWrapper
#
#
# class terminalXTest(unittest.TestCase):
#
#     def setUp(self):
#         self.chrome_options = webdriver.ChromeOptions()
#         # self.firefox_options = webdriver.FirefoxOptions()
#         # self.edge_options = webdriver.EdgeOptions()
#         self.browsers_list = [self.chrome_options]
#         self.my_api = APIWrapper()
#         self.url = "https://www.terminalx.com/pg/MutationAddAnyProductsToAnyCart"
#
#     def card_is_not_empty(self):
#         time.sleep(5)
#         try:
#             package_title = WebDriverWait(self.driver, 20).until(
#                 EC.visibility_of_element_located((By.XPATH, "//*[@id='app-root']/div[2]/main"
#                                                             "/div[2]/div/div/div[2]/div[1]/div[2]"))
#             )
#             return package_title.is_displayed()
#         except TimeoutException:
#             print("Timed out waiting for package title element to be visible")
#             return False
#
#     def test_parallel(self):
#         with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browsers_list)) as executor:
#             executor.map(self.test_check_card, self.browsers_list)
#
#     def test_check_card(self):
#         self.driver = webdriver.Chrome()
#
#         self.driver.get("https://www.terminalx.com/")
#         try:
#             card_button = WebDriverWait(self.driver, 20).until(
#                 EC.visibility_of_element_located((By.XPATH, "//*[@id='app-root']/div[2]/header/div[2]/div[4]/nav/ul/li[4]/a"))
#             )#"//*[@id='app-root']/div[2]/header/div/div[2]/div[3]/div/a[2]"
#             card_button.click()
#             time.sleep(5)
#         except Exception as e:
#             print(f"An error occurred: {e}")
#             # click on see the card
#         #     try:
#         #         card_button = WebDriverWait(self.driver, 20).until(
#         #             EC.visibility_of_element_located((By.XPATH, "// *[ @ id = 'top-portal-root']"
#         #                                                         " / div[1] / div / div / div[3] / a[2]"))
#         #         )
#         #         card_button.click()
#         #     except Exception as e:
#         #         print(f"An error occurred: {e}")
#         #
#         # self.assertTrue(self.card_is_not_empty(), "card is not empty")
#
#
# if __name__ == "__main__":
#     unittest.main()
