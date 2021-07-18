from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.checkstatus import CheckStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = CheckStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll("JavaScript for beginners")
        self.courses.enrollCourse(num="4645426832775134", exp="0226", cvv="882")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")
