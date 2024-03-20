import json
import os
import time
from os.path import dirname, join
from selenium import webdriver


class BrowserWrapper:
    def __init__(self):
        self.driver = None
        config_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'config_terminalX.json'))
        try:
            with open(config_file_path) as f:
                self.config = json.load(f)
        except FileNotFoundError:
            print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
            raise  # Raise the error to halt execution if the file is essential for the script to run
        self.browser_name = None
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")  # This line is often necessary in CI environments
        options.add_argument("--disable-dev-shm-usage")  # This can help in environments with limited resources
        self.driver = webdriver.Chrome(options=options)

    # return the webdriver based on the config file options
    def get_driver(self, browser):
        browser_type = self.config["browser"]
        if self.config["grid"]:
            options = self.set_up_capabilities(browser)
            self.driver = webdriver.Remote(command_executor=self.config["HAB_URL"], options=options)
            self.driver.fullscreen_window()

        else:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")  # This line is often necessary in CI environments
            options.add_argument("--disable-dev-shm-usage")  # This can help in environments with
            if browser.lower() == 'chrome':
                self.driver = webdriver.Chrome(options=options)
            elif browser.lower() == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser.lower() == 'edge':
                self.driver = webdriver.Edge()
        url = self.config["url"]

        self.driver.get(url)
        time.sleep(2)

        return self.driver

    def close_browser(self):
        if self.driver:
            self.driver.close()

    # return browser capabilities based on the browser
    def set_up_capabilities(self, browser_type):
        global options
        if browser_type.lower() == 'chrome':
            options = webdriver.ChromeOptions()
            self.add_options(options)
        elif browser_type.lower() == 'firefox':
            options = webdriver.FirefoxOptions()
            self.add_options(options)
        elif browser_type.lower() == 'edge':
            options = webdriver.EdgeOptions()
            self.add_options(options)
        platform_name = self.config["platform"]
        options.add_argument(f'--platformName={platform_name}')

        return options

    def is_parallel(self):
        return self.config["parallel"]

    # def close_browser(self):
    #     if self.driver:
    #         self.driver.quit()

    def get_browsers(self):
        return self.config["browser_types"]

    def get_filename(self, filename):
        here = dirname(__file__)
        output = join(here, filename)
        return output

    def is_grid(self):
        return self.config['grid']

    def get_browser(self):
        return self.config['browser']

    def goto(self, url):
        self.driver.get(url)

    def add_options(self, options):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
