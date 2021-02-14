import pytest
from base.webdriver_instance import WebDriverInstance
from pages.home.login_page import LoginPage
from utilities.read_data import get_csv_data


@pytest.yield_fixture(scope="class")
def run_app(browser):
    print("Running application")

    web_driver = WebDriverInstance(browser)
    driver = web_driver.get_webdriver_instance()

    user_data = get_csv_data("data/login_test_valid_data.csv")
    user_name = user_data[0][0]
    user_password = user_data[0][1]

    login_page = LoginPage(driver)
    login_page.login(user_name, user_password)

    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--osType")
