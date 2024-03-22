import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.BasePage import Base_Page
from logic.home_page import HomePage


class LoginPage(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)

    def login_flow(self):
        # Enter valid credentials
        username_field = self._driver.find_element(By.XPATH, "//*[@id='panel-root']/div/div[3]/div/div/div/div[3]/div["
                                                            "1]/div/form/div[1]/div/input")
        password_field = self._driver.find_element(By.XPATH, "//*[@id='panel-root']/div/div[3]/div/div/div/div[3]/div["
                                                            "1]/div/form/div[2]/div/input")
        submit_button = self._driver.find_element(By.XPATH, "//*[@id='panel-root']/div/div[3]/div/div/div/div[3]/div["
                                                           "1]/div/form/div[3]/button")

        username_field.send_keys("saeed.esawi99@gmail.com")  # Replace 'your_username' with actual username
        password_field.send_keys("Saeed@1234")  # Replace 'your_password' with actual password
        # Submit the login form
        submit_button.click()
        time.sleep(5)

    def login_page_displayed(self):
        login_ok = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='app-root']/div[2]/header/div/div[2]/div[1]/div[1]/div/div/div/button/span[2]"))
        )
        return login_ok.is_displayed()
