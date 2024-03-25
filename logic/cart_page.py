import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.ui_infra.BasePage import Base_Page


class CartPage(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.PACKAGE_TITLE = "//*[@id='app-root']/div[2]/main/div[2]/div/div/div[2]/div[1]/div[2]"
        self.LOGIN_BUTTON = "//*[@id='app-root']/div[2]/main/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/button"
        self.CART_TITLE = '//*[@id="app-root"]/div[2]/main/div[2]/div/div/div[2]/div/div'
        self.SALES_BUTTON = ('//*[@id="app-root"]/div[2]/main/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/div['
                             '1]/button')

    def card_is_not_empty(self):
        time.sleep(5)
        try:
            package_title = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, self.PACKAGE_TITLE))
            )
            return package_title.is_displayed()
        except TimeoutException:
            print("Timed out waiting for package title element to be visible")
            return False

    def click_checkout_page(self):
        login_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON))
        )

        # Click on the Login button
        login_button.click()

    def card_is_empty(self):
        time.sleep(5)
        try:
            cart_title = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, self.CART_TITLE))
            )
            return cart_title.is_displayed()
        except TimeoutException:
            print("Timed out waiting for package title element to be visible")
            return False

    def remove_item(self):
        try:
            sales_button = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH,self.SALES_BUTTON))
            )
            sales_button.click()
            time.sleep(5)
        except Exception as e:
            print(f"An error occurred: {e}")


