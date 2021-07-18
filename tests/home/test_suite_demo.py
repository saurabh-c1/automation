import unittest
from tests.home.login_tests import LoginTests
from tests.courses.register_courses_CSVData_tests import RegisterCoursesCSVDataTests

# Get all the test cases
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)

