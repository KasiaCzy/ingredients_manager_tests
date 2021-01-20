from selenium.webdriver.support.select import Select
from base.base_page import BasePage
import utilities.custom_logger as cl


class SearchRecipePage(BasePage):

    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_by_name_filed = "id_title"
    _select_box = "id_ingredient"
    _search_button = "//button[@type='submit']"
    _recipe_cards = "card-header text-center"
    _ingredient_list = "recipe-ingredients-list"
    _text = "empty-list-text"

    def enter_recipe_name(self, name):
        self.element_send_keys(name, self._search_by_name_filed)

    def select_ingredients(self, *args):
        select_box = self.get_element(self._select_box)
        sel = Select(select_box)
        for item in args:
            sel.select_by_visible_text(item)

    def click_search_button(self):
        self.element_click(self._search_button, locator_type="xpath")

    def search_recipe_by_name(self, string):
        self.clear_fields()
        self.enter_recipe_name(string)
        self.click_search_button()

    def search_recipe_by_ingredients(self, *args):
        self.clear_fields()
        self.select_ingredients(*args)
        self.click_search_button()

    def verify_search_by_name_success(self, string):
        recipe_cards = self.get_elements_list(self._recipe_cards, locator_type="class")

        return all(string in title.text for title in recipe_cards)

    def verify_search_by_ingredients_success(self, *args):
        recipes_ingredients_list = self.get_elements_list(self._ingredient_list, locator_type="class")
        for ingredient_list in recipes_ingredients_list:
            if not any(ingredient in ingredient_list.text for ingredient in args):
                return False
        return True

    def verify_recipe_not_found(self):
        return self.element_present(self._text, locator_type="class")

    def clear_fields(self):
        field = self.get_element(locator=self._search_by_name_filed)
        field.clear()
        select_box = self.get_element(self._select_box)
        sel = Select(select_box)
        sel.deselect_all()
