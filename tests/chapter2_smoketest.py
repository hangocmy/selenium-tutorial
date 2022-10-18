import unittest
import HTMLTestRunner
from chapter2 import SearchTests
from chapter2_2 import SignIn


#get all tests from SearchProductTest and HomePageTest class
test_search = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
test_sign_in = unittest.TestLoader().loadTestsFromTestCase(SignIn)

#create a test suite combining search_test and get_started_tests
smoke_tests = unittest.TestSuite([test_search, test_sign_in])


#configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(combine_reports=True, report_name="SmokeTestReport")

#run the suite using HTMLTestRunner
runner.run(smoke_tests)

