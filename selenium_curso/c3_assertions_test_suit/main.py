from unittest import TestLoader, TestSuite
from assertions import AssertionsTest
from searchtests import SearchTests
from HtmlTestRunner import HTMLTestRunner

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_tests = TestLoader().loadTestsFromTestCase(SearchTests)

# contruimos la suite de pruebas
smoke_test = TestSuite([assertions_test, search_tests])


# Aquí generamos nuestros reportes
kwargs = {
    "output": "reports/reportes",
    "report_name": "c3_assertions_test_suit",
    "combine_reports": True,
    "add_timestamp": False
    }


runner = HTMLTestRunner(**kwargs)

runner.run(smoke_test)
