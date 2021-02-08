from selenium.webdriver.common.by import By
from base.base_page import BasePage
import utilities.custom_logger as cl


class NavigationPage(BasePage):

    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _main_page = "CookingManager"
    _use_up_today = "Use up today"
    _keep_track = "Keep track"
    _recipes = "Recipes"

    def navigate_to_main_page(self):
        self.element_click(locator=self._main_page, locator_type=By.LINK_TEXT)

    def navigate_to_use_up_today(self):
        self.element_click(locator=self._use_up_today, locator_type=By.LINK_TEXT)

    def navigate_to_keep_track(self):
        self.element_click(locator=self._keep_track, locator_type=By.LINK_TEXT)

    def navigate_to_recipes(self):
        self.element_click(locator=self._recipes, locator_type=By.LINK_TEXT)