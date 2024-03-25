import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.ui_infra.BasePage import Base_Page


class BrandsPage(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.NIKE_TITLE = "//*[@id='app-root']/div[2]/main/div[2]/div/div[3]"
        self.SEARCH_TITLE = ("//*[@id='app-root']/div[2]/main/div[2]/div/div[3]/div[3]/div[2]/ol/li[5]/div[3]/div["
                             "1]/div[2]/span")
        self.PACKAGE_TITLE = "//*[@id='app-root']/div[2]/main/div[2]/div/div[1]/div/h1"
        self.SORT_BUTTON = ("//div[@class='listing-main_byCk']//div[@class='sortby-white_3sWp "
                            "rtl_1Wy3']")
        self.LOWER_TO_HEIGHT_BUTTON = "//option[@value='price_asc']"
        self.FINAL_PRICE_BUTTON = "(//div[@class='listing-content_2Leu']//div[contains(@class, 'final-price_8CiX')])[1]"
        self.FIRST_ITEM_BUTTON = ('(//div[@class="listing-content_2Leu"]//div[contains(@class, '
                                  '"final-price_8CiX")])[1]')
        self.SECOND_ITEM_BUTTON = ('(//div[@class="listing-content_2Leu"]//div[contains(@class, '
                                   '"final-price_8CiX")])[2]')

    def search_keys_failed_is_displayed(self):
        time.sleep(5)
        try:
            nike_title = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, self.NIKE_TITLE))
            )
            return nike_title.is_displayed()
        except TimeoutException:
            print("Timed out waiting for package title element to be visible")
            return False

    def search_is_displayed(self):
        time.sleep(5)
        try:
            search_title = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, self.SEARCH_TITLE))
            )
            return search_title.is_displayed()
        except TimeoutException:
            print("Timed out waiting for package title element to be visible")
            return False

    def on_sale_is_displayed(self):
        time.sleep(5)
        try:
            package_title = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, self.PACKAGE_TITLE))
            )
            return package_title.is_displayed()
        except TimeoutException:
            print("Timed out waiting for package title element to be visible")
            return False

    def sort_by_brand(self):
        time.sleep(2)
        sort_button = self._driver.find_element(By.XPATH, self.SORT_BUTTON)
        sort_button.click()
        lowest_price_to_highest_button = self._driver.find_element(By.XPATH, self.LOWER_TO_HEIGHT_BUTTON)
        lowest_price_to_highest_button.click()
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, self.FINAL_PRICE_BUTTON))
        )
        time.sleep(5)

    def convert_price_to_float(self, price_str):
        cleaned_price = ''.join(c for c in price_str if c.isdigit() or c == '.')
        return float(cleaned_price)

    def first_item_price(self):
        first_item_price = self._driver.find_element(By.XPATH,
                                                     self.FIRST_ITEM_BUTTON).text
        return self.convert_price_to_float(first_item_price)

    def second_item_price(self):
        second_item_price = self._driver.find_element(By.XPATH,
                                                      self.SECOND_ITEM_BUTTON).text
        return self.convert_price_to_float(second_item_price)

    def sort_isDisplayed(self):
        if self.first_item_price() <= self.second_item_price():
            return True
        else:
            return False

    def click_planket(self):
        blanket_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='app-root']/div[2]/main/div[2]/div/div[3]/div[3]/div[2]/ol/li[5]/div[2]/a/div/div/img"))
        )

        # Click on the Login button
        blanket_button.click()

    def click_add_planket(self):
        blanket_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='app-root']/div[2]/main/div[2]/div/div/div[2]/div[1]/div[2]/div/div[4]/button"))
        )

        # Click on the Login button
        blanket_button.click()
