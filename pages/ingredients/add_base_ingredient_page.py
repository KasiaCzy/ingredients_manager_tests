from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_page import BasePage
import utilities.custom_logger as cl
from utilities.util import Util


class AddBaseIngredientPage(BasePage):

    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.utility = Util()

    # Locators
    _add_ingredient_button = "//a[@href='/add_ingredient/']"
    _name_field = "id_name"
    _unit_field = "id_unit"
    _category_field = "id_category"
    _add_button = "//button[@name='submit']"
    _add_page_header = "page-header"
    _keep_track_page_header = "//h2[@class='text-center my-3']"

    def click_add_ingredient_button(self):
        if self.element_present(self._add_ingredient_button, locator_type=By.XPATH):
            self.element_click(self._add_ingredient_button, locator_type=By.XPATH)

    def enter_name_field(self, name):
        self.element_send_keys(name, self._name_field)

    def select_item(self, item, select_box_path):
        select_box = self.get_element(select_box_path)
        sel = Select(select_box)
        if type(item) == str:
            sel.select_by_visible_text(item)
        elif type(item) == int:
            sel.select_by_index(item)

    def click_add_button(self):
        self.element_click(self._add_button, locator_type=By.XPATH)

    def add_base_ingredient(self, name='', unit='', category=''):
        self.click_add_ingredient_button()
        self.clear_fields()
        self.enter_name_field(name)
        self.select_item(unit, self._unit_field)
        self.select_item(category, self._category_field)
        self.click_add_button()

    def verify_add_base_ingredient_success(self, name):
        element = self.get_element(f"//table//td[2][contains(text(),'{name}')]",
                                   locator_type=By.XPATH)
        result = self.element_present(element=element)
        return result

    def verify_add_base_ingredient_failed(self):
        page_header_text = self.get_element_text(self._add_page_header, locator_type=By.CLASS_NAME)
        return self.utility.verify_text_contains(page_header_text, "Add ingredient")

    def verify_keep_track_page(self):
        page_header_text = self.get_element_text(self._keep_track_page_header, locator_type=By.XPATH)
        return self.utility.verify_text_contains(page_header_text, "If you want to know what ingredients you have")

    def clear_fields(self):
        name_field = self.get_element(locator=self._name_field)
        name_field.clear()
        self.select_item(1, self._unit_field)
        self.select_item(1, self._category_field)
