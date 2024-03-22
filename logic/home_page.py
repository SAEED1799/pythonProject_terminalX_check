import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.BasePage import Base_Page


class HomePage(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)

    def click_login(self):
        login_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='app-root']/div[2]/header/div/div[2]/div[1]"))
        )

        # Click on the Login button
        login_button.click()