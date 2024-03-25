import json

import requests

from infra.ui_infra.BasePage import Base_Page


class AbiGetData(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)

    def get_cookie_conf(self):
        config_file_path = "C:\\Users\\hp\\PycharmProjects\\pythonProject5_terminalX_check\\utils\\config_terminalX.json"

        # Open the config file and read its contents
        with open(config_file_path, "r") as file:
            self.config_data = json.load(file)
        self.response = None
        self.my_request = requests
        return self.config_data['my_Cookie']

    def get_body_conf_add_item(self):
        config_file_path = "C:\\Users\\hp\\PycharmProjects\\pythonProject5_terminalX_check\\utils\\config_terminalX.json"

        # Open the config file and read its contents
        with open(config_file_path, "r") as file:
            self.config_data = json.load(file)
        self.response = None
        self.my_request = requests
        return self.config_data['body_add_item']