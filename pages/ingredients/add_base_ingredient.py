from selenium.webdriver.support.select import Select
from base.base_page import BasePage
import utilities.custom_logger as cl


class AddBaseIngredientPage(BasePage):

    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _add_ingredient_button = "//a[@href='/add_ingredient/']"
    _name_field = "id_name"
    _unit_field = "id_unit"
    _category_field = "id_category"
    _add_button = "//button[@name='submit']"
    _page_header = "page-header"

    def click_add_ingredient_button(self):
        if self.element_present(self._add_ingredient_button, locator_type="xpath"):
            self.element_click(self._add_ingredient_button, locator_type="xpath")

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
        self.element_click(self._add_button, locator_type="xpath")

    def add_base_ingredient(self, name='', unit='', category=''):
        self.click_add_ingredient_button()
        self.clear_fields()
        self.enter_name_field(name)
        self.select_item(unit, self._unit_field)
        self.select_item(category, self._category_field)
        self.click_add_button()

    def verify_add_base_ingredient_success(self, name):
        element = self.get_element(f"//table//td[2][contains(text(),'{name}')]",
                                   locator_type="xpath")
        result = self.element_present(element=element)
        return result

    def verify_add_base_ingredient_failed(self):
        result = self.element_present(self._page_header, locator_type='class')
        return result

    def verify_keep_track_page(self, header):
        return self.element_present(f"//h2[contains(text(), '{header}')]", locator_type="xpath")

    def clear_fields(self):
        name_field = self.get_element(locator=self._name_field)
        name_field.clear()
        self.select_item(1, self._unit_field)
        self.select_item(1, self._category_field)
