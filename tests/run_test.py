import unittest
import os
from datetime import datetime
import time
import html

# Import your test modules
from tests.functional_tests import test_case_2_negative, test_check_price, test_Check_Sale_Page_Is_OK, test_log_in, \
    test_remove_item, test_search_is_good, title_test
from tests.api_tests import test_api_page
from tests.test_api_continue_ui import test_add_api_check_ui

class HTMLReportTestRunner:
    def __init__(self, report_file):
        self.report_file = report_file

    def run(self, test_suite):
        start_time = time.time()
        with open(self.report_file, "w", encoding="utf-8") as f:
            # Initialize HTML Report
            f.write("<html><head>")
            f.write("<title>Test Report</title>")
            f.write("</head><body>")
            f.write("<h1>Test Execution Report</h1>")
            f.write("<table border='1'>")
            f.write("<thead>")
            f.write("<tr><th>Test Case</th><th>Status</th><th>Details</th></tr>")
            f.write("</thead><tbody>")

            # Custom TestResult
            class CustomTestResult(unittest.TestResult):
                def addSuccess(self, test):
                    super().addSuccess(test)
                    f.write(f"<tr><td>{test.id()}</td><td>Pass</td><td></td></tr>")

                def addError(self, test, err):
                    super().addError(test, err)
                    error_message = html.escape(self._exc_info_to_string(err, test))
                    f.write(f"<tr><td>{test.id()}</td><td>Error</td><td>{error_message}</td></tr>")

                def addFailure(self, test, err):
                    super().addFailure(test, err)
                    failure_message = html.escape(self._exc_info_to_string(err, test))
                    f.write(f"<tr><td>{test.id()}</td><td>Fail</td><td>{failure_message}</td></tr>")

            result = CustomTestResult()
            test_suite.run(result)

            # Finalize HTML Report
            end_time = time.time()
            total_time = end_time - start_time
            f.write("</tbody></table>")
            f.write(f"<h2>Summary</h2><p>Ran {result.testsRun} tests in {total_time:.2f}s</p>")
            if not result.wasSuccessful():
                f.write(f"<p><strong>FAILED</strong> (failures={len(result.failures)}, errors={len(result.errors)})</p>")
            else:
                f.write("<p>All tests passed.</p>")
            f.write("</body></html>")

if __name__ == "__main__":
    suite = unittest.TestSuite()

    test_modules = [
        test_add_api_check_ui, title_test, test_search_is_good,
        test_log_in, test_Check_Sale_Page_Is_OK, test_check_price,
        test_case_2_negative, test_api_page
    ]

    for module in test_modules:
        suite.addTests(unittest.TestLoader().loadTestsFromModule(module))

    report_dir = "./test_reports"
    os.makedirs(report_dir, exist_ok=True)
    report_file_name = f"TestReport_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html"
    report_file = os.path.join(report_dir, report_file_name)

    runner = HTMLReportTestRunner(report_file)
    runner.run(suite)

    print(f"Report generated: {report_file}")
