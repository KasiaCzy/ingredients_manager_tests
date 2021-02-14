from pages.home.register_page import RegisterPage
from utilities.test_status import Status
import pytest
import time
from utilities.read_data import get_csv_data


@pytest.mark.usefixtures("run_app", "log_out")
class TestRegister:

    @pytest.fixture(autouse=True)
    def class_set_up(self, run_app):
        self.driver = run_app
        self.register_page = RegisterPage(self.driver)
        self.test_status = Status(self.driver)

    @pytest.fixture()
    def log_out(self):
        self.register_page.logout()

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("user_name,user_password,conf_password",
                             get_csv_data("data/registration_test_valid_data.csv"))
    def test_valid_registration(self, user_name, user_password, conf_password):
        unique_user_name = user_name + str(round(time.time()*100))
        self.register_page.register(unique_user_name, user_password, conf_password)
        self.test_status.mark(self.register_page.verify_displayed_page_title(), "Title Verified")
        result = self.register_page.verify_register_success(unique_user_name)
        self.test_status.mark_final("test_valid_registration", result, "Registration was successful")

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("user_name,user_password,conf_password",
                             get_csv_data("data/registration_test_invalid_data.csv"))
    def test_invalid_registration_data(self, user_name, user_password, conf_password):
        self.register_page.register(user_name, user_password, conf_password)
        result = self.register_page.verify_invalid_data_register_failed()
        self.test_status.mark_final("test_invalid_registration_data", result, "Registration failed")

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("user_name,user_password,conf_password",
                             get_csv_data("data/registration_test_empty_data.csv"))
    def test_empty_registration_data(self, user_name, user_password, conf_password):
        self.register_page.register(user_name, user_password, conf_password)
        result = self.register_page.verify_empty_data_register_failed()
        self.test_status.mark_final("test_empty_registration_data", result, "Registration failed")
