import time

from selenium.webdriver.chrome import webdriver

from infra.api_infra.api_test_base import APITestBase
from logic.api_page import UserPage
from logic.cart_page import CartPage
from logic.home_page import HomePage
from logic.login_page import LoginPage
from selenium import webdriver


class AddToCart(APITestBase):

    def setUp(self):
        self.base_url = self.config['Tests']['baseURL']
        self.email = self.config['Tests']['loginCredentials']['email']
        self.password = self.config['Tests']['loginCredentials']['password']
        self.expected_user_name = self.config['Tests']['loginCredentials']['expected_user_name']
        self.customer_id = self.config['Tests']['customerInfo']['customer_id']
        self.qty = self.config['Tests']['product']['qty']
        self.sku = self.config['Tests']['product']['sku']
        self.qty_update = self.config['Tests']['product']['qty_update']
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.terminalx.com/")

    def test_add_item_to_cart(self):
        # Arrange
        # Log in and get cookies
        response, private_content_version_cookie, counter_cookie, PHPSESSID_cookie = UserPage.login(
            self.base_url, self.email, self.password)
        assert response['data']['userLogin']['customer_id'] == self.customer_id, "Login failed or customer_id mismatch"

        # Get user cart info to check for existing items
        response = UserPage.get_user_cart_info(
            self.base_url, private_content_version_cookie, counter_cookie, PHPSESSID_cookie)

        # If there are items in the cart, remove them
        if response['data']['currentUserInfo']['cart_object']['items']:
            item_id = response['data']['currentUserInfo']['cart_object']['items'][0]['id']
            response = UserPage.remove_item_from_cart(
                self.base_url, private_content_version_cookie, counter_cookie, PHPSESSID_cookie, item_id)
            assert response['data']['removeItemFromAnyCart']['total_quantity'] == 0, "Failed to empty the cart"

        # Act
        # Add an item to the cart
        response = UserPage.add_to_cart(
            self.base_url, self.qty, self.sku, private_content_version_cookie, counter_cookie, PHPSESSID_cookie)
        time.sleep(5)

        # Assert
        # Verify the item was added to the cart with the correct quantity
        actual_quantity = response['data']['addAnyProductsToAnyCart']['total_quantity']
        assert actual_quantity == self.qty, f"Expected quantity {self.qty}, but got {actual_quantity}"
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.home_page.click_login()
        self.login_page.login_flow()
        # self.my_api.api_post_request(self.url_add_to_cart, self.get_data.get_body_conf_add_item(),
        #                              self.get_data.get_cookie_conf())
        time.sleep(5)
        self.home_page.click_on_cart_button()
        self.home_page.click_go_to_card_button()
        self.assertTrue(self.cart_page.card_is_not_empty(), "card is not empty")

    def test_check_remove_item(self):
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.home_page.click_login()
        self.login_page.login_flow()
        self.home_page.click_on_cart_button()
        self.home_page.click_go_to_card_button()
        self.cart_page.remove_item()
        self.assertTrue(self.cart_page.card_is_empty(), "card is empty")
