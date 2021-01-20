import pytest
from base.webdriver_factory import WebDriverFactory
from pages.home.login_page import LoginPage


@pytest.yield_fixture()
def set_up():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def one_time_set_up(request, browser):
    print("Running one time setUp")
    web_driver = WebDriverFactory(browser)
    driver = web_driver.get_webdriver_instance()
    login_page = LoginPage(driver)
    login_page.login("im_admin", "im_project")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--osType")
