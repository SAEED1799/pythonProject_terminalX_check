import concurrent.futures
import unittest
from selenium import webdriver


class GulliverTitleTest(unittest.TestCase):

    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.firefox_options = webdriver.FirefoxOptions()
        self.edge_options = webdriver.EdgeOptions()
        self.browsers_list = [self.chrome_options, self.firefox_options,self.edge_options]

    def test_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browsers_list)) as executor:
            executor.map(self.test_title, self.browsers_list)

    def test_title(self,options):
        # Initialize WebDriver (in this case, Chrome)
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)

        # Open the Gulliver website
        driver.get("https://www.terminalx.com/")


if __name__ == "__main__":
    unittest.main()
