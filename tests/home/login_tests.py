from pages.home.login_page import LoginPage
from utilities.test_status import Status
import pytest
from utilities.read_data import get_csv_data


@pytest.mark.usefixtures("run_app")
class TestLogin:

    @pytest.fixture(autouse=True)
    def class_set_up(self, run_app):
        self.driver = run_app
        self.login_page = LoginPage(self.driver)
        self.test_status = Status(self.driver)

    @pytest.fixture()
    def log_out(self):
        self.login_page.logout()

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("user_name,user_password", get_csv_data("login_test_valid_data.csv"))
    def test_valid_login(self, user_name, user_password, log_out):
        self.login_page.login(user_name, user_password)
        self.test_status.mark(self.login_page.verify_logged_page_title(), "Title Verified")
        result = self.login_page.verify_login_success(user_name)
        self.test_status.mark_final("test_valid_login", result, "Login was successful")

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("user_name,user_password", get_csv_data("login_test_invalid_data.csv"))
    def test_invalid_login_data(self, user_name, user_password, log_out):
        self.login_page.login(user_name, user_password)
        result = self.login_page.verify_invalid_data_login_failed()
        self.test_status.mark_final("test_invalid_login_data", result, "Login failed")

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("user_name,user_password", get_csv_data("login_test_empty_data.csv"))
    def test_empty_login_data(self, user_name, user_password, log_out):
        self.login_page.login(user_name, user_password)
        result = self.login_page.verify_empty_data_login_failed()
        self.test_status.mark_final("test_empty_login_data", result, "Login failed")
