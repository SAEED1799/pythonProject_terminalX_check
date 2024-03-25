import unittest

import HtmlTestRunner

from tests.functional_tests import test_case_2_negative, test_check_price, test_Check_Sale_Page_Is_OK, test_log_in, \
    test_search_is_good, title_test
from tests.api_tests import test_api_page
from tests.test_api_continue_ui import test_add_api_check_ui

if __name__ == "__main__":
    # Create a test suite combining all test cases
    suite = unittest.TestSuite()

    # Load tests from each test module
    for module in (test_add_api_check_ui, title_test, test_search_is_good,
                   test_log_in, test_Check_Sale_Page_Is_OK, test_check_price, test_case_2_negative,
                   test_api_page):
        suite.addTests(unittest.TestLoader().loadTestsFromModule(module))

    # Run the test suite
    #runner = unittest.TextTestRunner(verbosity=2)
    runner = HtmlTestRunner.HTMLTestRunner(output='test-reports')
    runner.run(suite)
