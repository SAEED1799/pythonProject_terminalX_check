import json
import os

import requests
import logging


class APIWrapper:

    def __init__(self):
        config_file_path = "C:\\Users\\hp\\PycharmProjects\\pythonProject5_terminalX_check\\utils\\config_terminalX.json"

        # Open the config file and read its contents
        with open(config_file_path, "r") as file:
            self.config_data = json.load(file)
        self.response = None
        self.my_request = requests
        self.logger = logging.getLogger(__name__)

    def api_get_request(self, url, body=None, header=None):
        self.logger.info(f"Making GET request to {url} with body: {body}")
        self.response = self.my_request.get(url, params=body, headers=header)
        self.logger.info(f"Received response: {self.response.status_code}")
        return self.response

    def api_post_request(self, url, body=None, header=None):
        headers = self.config_data['my_Cookie']
        body = self.config_data['body_add_item']
        self.logger.info(f"Making POST request to {url} with body: {body}")
        self.response = self.my_request.post(url, json=body, headers=headers)
        self.logger.info(f"Received response: {self.response.status_code}")
        return self.response

    def api_put_request(self, url, body=None, header=None):
        self.logger.info(f"Making PUT request to {url} with body: {body}")
        self.response = self.my_request.put(url, params=body, headers=header)
        self.logger.info(f"Received response: {self.response.status_code}")
        return self.response
