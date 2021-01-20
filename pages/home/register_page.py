from base.base_page import BasePage
from pages.home.navigation_page import NavigationPage
import utilities.custom_logger as cl


class RegisterPage(BasePage):

    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.navigation_page = NavigationPage(driver)

    # Locators
    _register_button = "//a[@href='/users/register/' and @role='button']"
    _username_field = "id_username"
    _register_password_field = "id_password1"
    _register_password_field_conf = "id_password2"
    _submit_button = "//button[@name='submit']"
    _register_link = "//a[@class='nav-link' and @href='/users/register/']"
    _logout_link = "Log out"

    def click_register_button(self):
        if self.element_present(self._register_button, locator_type="xpath"):
            self.element_click(self._register_button, locator_type="xpath")

    def enter_username_field(self, username):
        self.element_send_keys(username, self._username_field)

    def enter_password_field(self, password, password_conf):
        self.element_send_keys(password, self._register_password_field)
        self.element_send_keys(password_conf, self._register_password_field_conf)

    def click_submit_button(self):
        self.element_click(self._submit_button, locator_type="xpath")

    def register(self, username="", password="", password_conf=""):
        self.click_register_button()
        self.clear_fields()
        self.enter_username_field(username)
        self.enter_password_field(password, password_conf)
        self.click_submit_button()

    def clear_fields(self):
        username_field = self.get_element(locator=self._username_field)
        username_field.clear()
        password_field = self.get_element(locator=self._register_password_field)
        password_field.clear()
        password_field_conf = self.get_element(locator=self._register_password_field_conf)
        password_field_conf.clear()

    def verify_register_success(self, username):
        result = self.element_present(f"//span[contains(text(), 'Hello, {username}')]", locator_type="xpath")
        return result

    def verify_register_failed(self):
        result = self.element_present(self._register_link, locator_type="xpath")
        return result

    def verify_register_title(self):
        return self.verify_page_title("Cooking Manager")

    def logout(self):
        self.element_click(locator=self._logout_link, locator_type="link")
        self.navigation_page.navigate_to_main_page()
