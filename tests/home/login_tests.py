from pages.home.login_page import LoginPage
from utilities.test_status import Status
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import get_csv_data


@pytest.mark.usefixtures("one_time_set_up", "set_up")
@ddt
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_set_up(self, one_time_set_up):
        self.login_page = LoginPage(self.driver)
        self.test_status = Status(self.driver)

    @pytest.mark.run(order=2)
    @data(*get_csv_data("login_test_valid_data.csv"))
    @unpack
    def test_valid_login(self, user_name, user_password):
        # self.lp.logout()
        self.login_page.login(user_name, user_password)
        result1 = self.login_page.verify_login_title()
        self.test_status.mark(result1, "Title Verified")
        result2 = self.login_page.verify_login_success(user_name)
        self.test_status.mark_final("test_valid_login", result2, "Login was successful")

    @pytest.mark.run(order=1)
    @data(*get_csv_data("login_test_invalid_data.csv"))
    @unpack
    def test_invalid_login(self, user_name, user_password):
        self.login_page.logout()
        self.login_page.login(user_name, user_password)
        result = self.login_page.verify_login_failed()
        self.test_status.mark_final("test_invalid_login", result, "Login failed")
        # assert result == True
