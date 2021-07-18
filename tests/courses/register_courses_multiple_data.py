from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.checkstatus import CheckStatus
import unittest
import pytest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = CheckStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "4645426832775134", "0226", "882"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")
        self.driver.find_element_by_link_text("ALL COURSES").click()
