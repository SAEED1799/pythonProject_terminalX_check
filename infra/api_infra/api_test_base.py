import unittest
import json
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options


class APITestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config_path = "C:\\Users\\hp\\PycharmProjects\\pythonProject5_terminalX_check\\utils\\api_config.json"
        # Load the test configuration
        with open(config_path, encoding='utf-8') as config_file:
            cls.config = json.load(config_file)
