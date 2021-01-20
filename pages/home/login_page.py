from base.base_page import BasePage
from pages.home.navigation_page import NavigationPage
import utilities.custom_logger as cl


class LoginPage(BasePage):

    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.navigation_page = NavigationPage(driver)

    # Locators
    _login_button = "//a[@href='/users/login/' and @role='button']"
    _username_field = "id_username"
    _login_password_field = "id_password"
    _submit_button = "//button[@name='submit']"
    _login_link = "//a[@class='nav-link' and @href='/users/login/']"
    _logout_link = "Log out"

    def click_login_button(self):
        if self.element_present(self._login_button, locator_type="xpath"):
            self.element_click(self._login_button, locator_type="xpath")

    def enter_username_field(self, username):
        self.element_send_keys(username, self._username_field)

    def enter_password_field(self, password):
        self.element_send_keys(password, self._login_password_field)

    def click_submit_button(self):
        self.element_click(self._submit_button, locator_type="xpath")

    def login(self, username="", password=""):
        self.click_login_button()
        self.clear_fields()
        self.enter_username_field(username)
        self.enter_password_field(password)
        self.click_submit_button()

    def verify_login_success(self, username):
        result = self.element_present(f"//span[contains(text(), 'Hello, {username}')]", locator_type="xpath")
        return result

    def verify_login_failed(self):
        result = self.element_present(self._login_link, locator_type="xpath")
        return result

    def verify_login_title(self):
        return self.verify_page_title("Cooking Manager")

    def clear_fields(self):
        username_field = self.get_element(locator=self._username_field)
        username_field.clear()
        password_field = self.get_element(locator=self._login_password_field)
        password_field.clear()

    def logout(self):
        self.element_click(locator=self._logout_link, locator_type="link")
        self.navigation_page.navigate_to_main_page()
