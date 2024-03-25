from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.ui_infra.BasePage import Base_Page


class Check_Out_Page(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.SUBMIT_CONTINUE_BUTTON = "//*[@id='app-root']/div[2]/main/div[2]/div/section/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/button"
        self.NEW_ADDRESS_BUTTON = "//*[@id='app-root']/div[2]/main/div[2]/div/section/div[2]/div[1]/div[3]/div[3]/div[2]/div/div/button"
        self.FIRST_NAME = "//*[@id='app-root']/div[2]/main/div[2]/div/section/div[2]/div[1]/div[3]/div[3]/div[2]/div/div[2]/div/form/div[1]/div[1]/div[1]/div/input"
        self.LAST_NAME = "//*[@id='app-root']/div[2]/main/div[2]/div/section/div[2]/div[1]/div[3]/div[3]/div[2]/div/div[2]/div/form/div[1]/div[1]/div[2]/div/input"
        self.CITY = "//*[@id='downshift-2-input']"
        self.STREET = "//*[@id='downshift-3-input']"
        self.NUM_STREET = "//*[@id='app-root']/div[2]/main/div[2]/div/section/div[2]/div/div[3]/div[3]/div[2]/div/form/div[2]/div[3]/div/input"
        self.PHONE_NUMBER = "//*[@id='app-root']/div[2]/main/div[2]/div/section/div[2]/div/div[3]/div[3]/div[2]/div/form/div[3]/div[2]/div/div/input"
        self.SUBMIT_LAST_OK = "//*[@id='app-root']/div[2]/main/div[2]/div/section/div[2]/div/div[3]/div[3]/div[2]/div/form/div[7]/button"

    def insert_keys(self):
        wait = WebDriverWait(self._driver, 10)  # Adjust the timeout as necessary

        # Click the 'Continue' button
        submit_continue_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                        self.SUBMIT_CONTINUE_BUTTON)))
        submit_continue_button.click()

        new_address_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                    self.NEW_ADDRESS_BUTTON)))
        new_address_button.click()

        # Fill out the form
        first_name = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                  self.FIRST_NAME)))
        last_name = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                 self.LAST_NAME)))
        city = wait.until(EC.visibility_of_element_located((By.XPATH, self.CITY)))
        street = wait.until(EC.visibility_of_element_located((By.XPATH, self.STREET)))
        num_street = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                  self.NUM_STREET)))
        phone_number = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                    self.PHONE_NUMBER)))

        first_name.send_keys("bfs")
        last_name.send_keys("3245")
        city.send_keys("כפר ברא")
        street.send_keys("אבן רושד")
        num_street.send_keys("3")
        phone_number.send_keys("0504178596")

        # Submit the form
        submit_button_last_ok = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                       self.SUBMIT_LAST_OK)))
        submit_button_last_ok.click()
