from pages.recipes.add_recipe_page import AddRecipePage
from utilities.test_status import Status
from pages.home.navigation_page import NavigationPage
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import get_csv_data


@pytest.mark.usefixtures("one_time_set_up", "set_up")
@ddt
class AddRecipeTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_set_up(self, one_time_set_up):
        self.recipe_page = AddRecipePage(self.driver)
        self.test_status = Status(self.driver)
        self.navigation_page = NavigationPage(self.driver)

    def setUp(self):
        self.navigation_page.navigate_to_recipes()

    @pytest.mark.run(order=2)
    @data(*get_csv_data("add_recipe_valid_data.csv"))
    @unpack
    def test_valid_add_recipe(self, title, link, *ingredients):
        self.recipe_page.add_recipe(title, link, *ingredients)
        result1 = self.recipe_page.verify_recipes_page("Recipes")
        self.test_status.mark(result1, "Page Header Verified")
        result2 = self.recipe_page.verify_add_recipe_success("Caramel apple buns")
        self.test_status.mark_final("test_valid_add_recipe", result2, "Adding recipe was successful")

    @pytest.mark.run(order=1)
    @data(*get_csv_data("add_recipe_invalid_data.csv"))
    @unpack
    def test_invalid_add_recipe(self, title, link, *ingredients):
        self.recipe_page.add_recipe(title, link, *ingredients)
        result = self.recipe_page.verify_add_recipe_failed()
        self.test_status.mark_final("test_invalid_add_recipe", result, "Add recipe failed")
