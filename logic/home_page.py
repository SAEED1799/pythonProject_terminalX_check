import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.ui_infra.BasePage import Base_Page


class HomePage(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.SEARCH_BUTTON = "//*[@id='app-root']/div[2]/header/div/div[4]/nav/ul/li[1]/button"
        self.SEARCH_BAR = ("//*[@id='app-root']/div[2]/header/div[2]/div[4]/nav/ul/li["
                           "1]/div/form/input")
        self.LOGIN_BUTTON = "//*[@id='app-root']/div[2]/header/div/div[2]/div[1]"
        self.CART_BUTTON = ("//*[@id='app-root']/div[2]/header/div"
                            "/div[2]/div[3]/div/a[2]")
        self.CART_INFO_BUTTON = "//*[@id='top-portal-root']/div[2]/div/div/div[3]/a[2]"
        self.SALE_BUTTON = ("//*[@id='app-root']/div[2]/"
                            "header/div/div[4]/nav/ul/li[4]/a")

    def search_btn(self):
        search_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.SEARCH_BUTTON))
        )

        # Click on the Login button
        search_button.click()
        time.sleep(5)

    def search_text(self, search_query):
        search_bar = self._driver.find_element(By.XPATH,
                                               self.SEARCH_BAR)  # Adjust the selector according to the site's
        # structure

        # 3. Enter a valid search query
        search_bar.send_keys(search_query)

        # 4. Initiate the search by clicking on the search button
        search_bar.send_keys(Keys.ENTER)

        # Allow time for the page to load
        time.sleep(3)  # It's better to use WebDriverWait instead of sleep

    def click_login(self):
        login_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON))
        )

        # Click on the Login button
        login_button.click()

    def click_on_cart_button(self):
        # click on cart
        try:
            card_button = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, self.CART_BUTTON))
            )
            card_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def click_go_to_card_button(self):
        # click on see the card
        try:
            card_in_button = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, self.CART_INFO_BUTTON))
            )
            card_in_button.click()
            time.sleep(5)
        except Exception as e:
            print(f"An error occurred: {e}")

    def click_on_sales_button(self):
        try:
            sales_button = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, self.SALE_BUTTON))
            )
            sales_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def go_to_category(self, category_name):
        """Navigate to a specified category page."""
        category_link_xpath = f"//a[contains(text(), '{category_name}')]"  # Example XPath, adjust as needed
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, category_link_xpath))
        )
        self._driver.find_element(By.XPATH, category_link_xpath).click()

    def is_loaded(self):
        """Check if the product details page has loaded."""
        # Example check: wait for the product title to be visible
        try:
            WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'product-title'))  # Adjust class name as needed
            )
            return True
        except:
            return False

    def perform_search(self, query):
        # Wait for the search button to be clickable and click it
        WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='search-button_1ENs']"))
        ).click()

        # Wait for the search input to be visible
        WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@class='input_sILM']"))
        )

        # Now that the search input is visible, we can find it and interact with it
        search_input = self._driver.find_element(By.XPATH, "//div[@class='search-results_2YMu']")
        search_input.clear()
        search_input.send_keys(query)
        time.sleep(5)  # Pause to visually confirm the input text
        search_input.send_keys(Keys.ENTER)
