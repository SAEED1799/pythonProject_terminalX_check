from infra.api_infra.api_test_base import APITestBase
from logic.api_page import UserPage


class AddToCartThroughAPI(APITestBase):

    def setUp(self):
        self.base_url = self.config['Tests']['baseURL']
        self.email = self.config['Tests']['loginCredentials']['email']
        self.password = self.config['Tests']['loginCredentials']['password']
        self.expected_user_name = self.config['Tests']['loginCredentials']['expected_user_name']
        self.customer_id = self.config['Tests']['customerInfo']['customer_id']
        self.qty = self.config['Tests']['product']['qty']
        self.sku = self.config['Tests']['product']['sku']
        self.qty_update = self.config['Tests']['product']['qty_update']

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

        # Assert
        # Verify the item was added to the cart with the correct quantity
        actual_quantity = response['data']['addAnyProductsToAnyCart']['total_quantity']
        assert actual_quantity == self.qty, f"Expected quantity {self.qty}, but got {actual_quantity}"

    def test_remove_item_from_cart(self):
        # Arrange
        # Log in and get cookies
        response, private_content_version_cookie, counter_cookie, PHPSESSID_cookie = UserPage.login(
            self.base_url, self.email, self.password)
        assert response['data']['userLogin']['customer_id'] == self.customer_id, "Login failed or customer_id mismatch"

        # Ensure there is at least one item in the cart to remove
        response = UserPage.get_user_cart_info(
            self.base_url, private_content_version_cookie, counter_cookie, PHPSESSID_cookie)
        if not response['data']['currentUserInfo']['cart_object']['items']:
            # Add an item if the cart is empty, for the sake of this test
            UserPage.add_to_cart(
                self.base_url, 1, 'some_sku', private_content_version_cookie, counter_cookie, PHPSESSID_cookie)

        # Get the item ID of the first item in the cart
        item_id = response['data']['currentUserInfo']['cart_object']['items'][0]['id']

        # Act
        # Attempt to remove the specified item from the cart
        response = UserPage.remove_item_from_cart(
            self.base_url, private_content_version_cookie, counter_cookie, PHPSESSID_cookie, item_id)

        # Assert
        # Verify the item has been removed from the cart
        assert response['data']['removeItemFromAnyCart'][
                   'total_quantity'] == 0, "Item was not successfully removed from the cart"

        # Optionally, you can verify the cart is empty if that's the expected result
        response = UserPage.get_user_cart_info(
            self.base_url, private_content_version_cookie, counter_cookie, PHPSESSID_cookie)
        assert not response['data']['currentUserInfo']['cart_object']['items'], "Cart is not empty after item removal"

    def test_get_cart_information(self):
        # Arrange
        # Log in and get cookies
        response, private_content_version_cookie, counter_cookie, PHPSESSID_cookie = UserPage.login(
            self.base_url, self.email, self.password)
        assert response['data']['userLogin']['customer_id'] == self.customer_id, "Login failed or customer_id mismatch"

        # Act
        # Retrieve the cart information
        response = UserPage.get_user_cart_info(
            self.base_url, private_content_version_cookie, counter_cookie, PHPSESSID_cookie)

        # Assert
        # Check for expected structure or data in the cart info
        assert 'currentUserInfo' in response['data'], "Cart information could not be retrieved"
        assert 'cart_object' in response['data']['currentUserInfo'], "Cart object is missing in the response"
        # Optionally, assert more specific details about the cart, such as item count, if applicable

    def test_login_pass(self):
        # Arrange
        response, private_content_version_cookie, counter_cookie, PHPSESSID_cookie = UserPage.login(
            self.base_url, self.email, self.password)
        assert 'customer_id' in response['data']['userLogin'], "Login failed or customer_id mismatch"

