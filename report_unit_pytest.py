import unittest

# Import test modules
from tests.functional_tests import test_case_2_negative, test_check_price, test_Check_Sale_Page_Is_OK


def create_suite():
    suite = unittest.TestSuite()

    # Load tests from the test modules
    for test_module in [test_case_2_negative, test_check_price, test_Check_Sale_Page_Is_OK]:
        # This assumes each module has a TestCase-derived class following the `unittest` pattern.
        suite.addTests(unittest.TestLoader().loadTestsFromModule(test_module))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = create_suite()
    runner.run(test_suite)
