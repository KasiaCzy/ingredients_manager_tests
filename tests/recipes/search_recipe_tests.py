from pages.recipes.search_recipe import SearchRecipePage
from pages.home.navigation_page import NavigationPage
from utilities.test_status import Status
from ddt import ddt, data, unpack
from utilities.read_data import get_csv_data
import unittest
import pytest


@pytest.mark.usefixtures("one_time_set_up", "set_up")
@ddt
class SearchRecipeTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_set_up(self):
        self.recipe_page = SearchRecipePage(self.driver)
        self.test_status = Status(self.driver)
        self.navigation_page = NavigationPage(self.driver)

    def setUp(self):
        self.navigation_page.navigate_to_recipes()

    @pytest.mark.run(order=2)
    def test_recipe_found_by_name(self):
        self.recipe_page.search_recipe_by_name("apple")
        result = self.recipe_page.verify_search_by_name_success("apple")
        self.test_status.mark_final("test_recipe_found_by_name", result, "Searching recipe by name was successful")
        # assert result == True

    @pytest.mark.run(order=1)
    def test_recipe_not_found_by_name(self):
        self.recipe_page.search_recipe_by_name("efek")
        result = self.recipe_page.verify_recipe_not_found()
        self.test_status.mark_final("test_recipe_not_found_by_name", result,
                           "No recipe was found. Searching recipe by not existing name was successful. ")
        # assert result == True

    @pytest.mark.run(order=3)
    @data(*get_csv_data("recipe_found_by_ingredients_data.csv"))
    @unpack
    def test_recipe_found_by_ingredients(self, *ingredients):
        self.recipe_page.search_recipe_by_ingredients(*ingredients)
        result = self.recipe_page.verify_search_by_ingredients_success(*ingredients)
        self.test_status.mark_final("test_recipe_found_by_ingredients", result, "Searching recipe by ingredients was successful")
        # assert result == True
