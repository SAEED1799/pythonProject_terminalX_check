import json

import requests
import logging


class APIWrapper:

    def __init__(self):
        self.response = None
        self.my_request = requests
        self.config = ""
        self.logger = logging.getLogger(__name__)

    def api_get_request(self, url, body=None, header=None):
        self.logger.info(f"Making GET request to {url} with body: {body}")
        self.response = self.my_request.get(url, params=body, headers=header)
        self.logger.info(f"Received response: {self.response.status_code}")
        return self.response

    def api_post_request(self, url, body=None, header=None):
        headers = {
            'Cookie': "syte_uuid=8aec36f0-e1e9-11ee-91fa-ab30a63932d8; _fbp=fb.1.1710410368098.1603310446; _tt_enable_cookie=1; _ttp=m8Q9hhUkfDKHM8NhnD7sXmYXewC; glassix-visitor-id-v2-b6d2bc1d-dcdc-4766-b620-28559157075a=ab845d32-8366-419f-b392-301556435cb0; wz.uid=q17SBw8Il61I267G510C17u58; current-universe-id-1=67; syte_ab_tests={}; _gid=GA1.2.1711495902.1710835220; slider_animation=1; fe-version=e7873e9ce8396ea08ef8d271a0853c2abcb0a228; RSESSIONID=6dd03188-02bd-4650-aa93-955052826a1c; language=he; counter=0; PHPSESSID=lva24ssdcb7qdtcq5jcf5sbdll; idus-cache-loggedin=1; _ga=GA1.1.539162828.1710410367; _uetsid=bbc9c2d0e5c611eeae02e7e838525cb6; _uetvid=8b8fa710e1e911ee878375296a5e3c47; _gcl_au=1.1.1432958371.1710410368.1620187912.1710930847.1710930853; _dc_gtm_UA-99383422-1=1; private_content_version=53076bb24746aa1c794a23c904ab8200; stimgs={%22sessionId%22:78393840%2C%22didReportCameraImpression%22:false%2C%22newUser%22:null}; _ga_Z2CGV88685=GS1.1.1710933771.13.0.1710933781.0.0.0"
        }
        body = {
            "cart_items": [
                {
                    "data": {
                        "quantity": 1,
                        "any_sku": "Z10291510603"
                    }
                }
            ],
            "skip_collect": 1
        }
        self.logger.info(f"Making POST request to {url} with body: {body}")
        self.response = self.my_request.post(url, json=body, headers=headers)
        self.logger.info(f"Received response: {self.response.status_code}")
        return self.response

    def api_put_request(self, url, body=None, header=None):
        self.logger.info(f"Making PUT request to {url} with body: {body}")
        self.response = self.my_request.put(url, params=body, headers=header)
        self.logger.info(f"Received response: {self.response.status_code}")
        return self.response
