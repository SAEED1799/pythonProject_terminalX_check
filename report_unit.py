import unittest
import HtmlTestRunner

# Import your specific test classes
from tests.functional_tests import test_case_2_negative, test_check_price, test_Check_Sale_Page_Is_OK, test_log_in, \
    test_remove_item, test_search_is_good, title_test
from tests.api_tests import test_api_page
from tests.test_api_continue_ui import test_add_api_check_ui

if __name__ == "__main__":
    # Create a test suite combining all test cases
    suite = unittest.TestSuite()

    # Assuming each module contains a TestCase class, add them to the suite
    # This part may need adjustments based on how your tests are structured
    for test_module in [test_case_2_negative, test_check_price, test_Check_Sale_Page_Is_OK, test_log_in,
                        test_search_is_good, title_test, test_api_page, test_add_api_check_ui]:
        for test_case in unittest.TestLoader().loadTestsFromModule(test_module):
            suite.addTest(test_case)

    # Define the directory where the HTML report will be saved
    report_dir = 'tests/test-reports'

    # Run the test suite with HtmlTestRunner to generate an HTML report
    runner = HtmlTestRunner.HTMLTestRunner(output=report_dir, report_title='Test Report', combine_reports=True,
                                           add_timestamp=True)
    runner.run(suite)
