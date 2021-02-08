from selenium.webdriver.common.by import By
from base.base_page import BasePage
import utilities.custom_logger as cl
from utilities.util import Util


class AddRecipePage(BasePage):

    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.utility = Util()

    # Locators
    _add_recipe_button = "//a[@href='/add_recipe/']"
    _title_field = "id_title"
    _link_field = "id_link"
    _checkbox_fields = "//input[@class='form-check-input']"
    _add_button = "//button[@name='submit']"
    _recipes_page_header = "//h1[@class='text-center my-3']"

    def click_add_recipe_button(self):
        if self.element_present(self._add_recipe_button, locator_type=By.XPATH):
            self.element_click(self._add_recipe_button, locator_type=By.XPATH)

    def enter_title_field(self, title):
        self.element_send_keys(title, self._title_field)

    def enter_link_field(self, link):
        self.element_send_keys(link, self._link_field)

    def assign_ingredients(self, ingredients):
        ingredients_list = ingredients.split(sep=',')
        for ingredient in ingredients_list:
            element = self.get_element(f"//label[contains(text(),'{ingredient}')]", locator_type=By.XPATH)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.element_click(element=element)

    def click_add_button(self):
        self.element_click(self._add_button, locator_type=By.XPATH)

    def add_recipe(self, title="", link="", ingredients=""):
        self.click_add_recipe_button()
        self.clear_fields()
        self.enter_title_field(title)
        self.enter_link_field(link)
        self.assign_ingredients(ingredients)
        self.web_scroll(direction="down")
        self.click_add_button()

    def verify_add_recipe_success(self, title):
        element = self.get_element(f"//div[@class='card-header text-center']/h5[contains(text(),'{title}')]",
                                   locator_type=By.XPATH)
        result = self.element_present(element=element)
        return result

    def verify_add_recipe_failed(self):
        result = self.element_present(self._title_field)
        return result

    def verify_recipes_page(self):
        page_header_text = self.get_element_text(self._recipes_page_header, locator_type=By.XPATH)
        return self.utility.verify_text_contains(page_header_text, "Recipes")

    def clear_fields(self):
        title_field = self.get_element(locator=self._title_field)
        title_field.clear()
        link_field = self.get_element(locator=self._link_field)
        link_field.clear()
        checkbox_fields = self.get_elements_list(self._checkbox_fields, locator_type=By.XPATH)
        for field in checkbox_fields:
            if field.is_selected():
                field.click()
