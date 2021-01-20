from pages.home.register_page import RegisterPage
from utilities.test_status import Status
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import get_csv_data


@pytest.mark.usefixtures("one_time_set_up", "set_up")
@ddt
class RegisterTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_set_up(self, one_time_set_up):
        self.register_page = RegisterPage(self.driver)
        self.test_status = Status(self.driver)

    @pytest.mark.run(order=2)
    @data(*get_csv_data("registration_test_valid_data.csv"))
    @unpack
    def test_valid_registration(self, user_name, user_password, conf_password):
        self.register_page.register(user_name, user_password, conf_password)
        result1 = self.register_page.verify_register_title()
        self.test_status.mark(result1, "Title Verified")
        result2 = self.register_page.verify_register_success("im_test")
        self.test_status.mark_final("test_valid_registration", result2, "Registration was successful")

    @pytest.mark.run(order=1)
    @data(*get_csv_data("registration_test_invalid_data.csv"))
    @unpack
    def test_invalid_registration(self, user_name, user_password, conf_password):
        self.register_page.logout()
        self.register_page.register(user_name, user_password, conf_password)
        result = self.register_page.verify_register_failed()
        self.test_status.mark_final("test_invalid_registration", result, "Registration failed")
        # assert result == True
