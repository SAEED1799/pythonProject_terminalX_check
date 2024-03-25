import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.ui_infra.BasePage import Base_Page


class LoginPage(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.USERNAME_FIELD = ("//*[@id='panel-root']/div/div[3]/div/div/div/div[3]/div["
                                                            "1]/div/form/div[1]/div/input")
        self.PASSWORD_FIELD = ("//*[@id='panel-root']/div/div[3]/div/div/div/div[3]/div["
                                                            "1]/div/form/div[2]/div/input")
        self.LOGIN_BUTTON = ("//*[@id='panel-root']/div/div[3]/div/div/div/div[3]/div["
                                                           "1]/div/form/div[3]/button")
        self.LOGIN_BUTTON_OK = "//*[@id='app-root']/div[2]/header/div/div[2]/div[1]/div[1]/div/div/div/button/span[2]"

    def login_flow(self):
        # Enter valid credentials
        username_field = self._driver.find_element(By.XPATH, "//*[@id='panel-root']/div/div[3]/div/div/div/div[3]/div["
                                                            "1]/div/form/div[1]/div/input")
        password_field = self._driver.find_element(By.XPATH, "//*[@id='panel-root']/div/div[3]/div/div/div/div[3]/div["
                                                            "1]/div/form/div[2]/div/input")
        submit_button = self._driver.find_element(By.XPATH, "//*[@id='panel-root']/div/div[3]/div/div/div/div[3]/div["
                                                           "1]/div/form/div[3]/button")
        time.sleep(5)
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
