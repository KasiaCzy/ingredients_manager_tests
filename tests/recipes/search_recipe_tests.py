from pages.recipes.search_recipe_page import SearchRecipePage
from pages.home.navigation_page import NavigationPage
from utilities.test_status import Status
from utilities.read_data import get_csv_data
import pytest


@pytest.mark.usefixtures("run_app", "navigate_page")
class TestSearchRecipe:

    @pytest.fixture(autouse=True)
    def class_set_up(self, run_app):
        self.driver = run_app
        self.recipe_page = SearchRecipePage(self.driver)
        self.test_status = Status(self.driver)
        self.navigation_page = NavigationPage(self.driver)

    @pytest.fixture()
    def navigate_page(self):
        self.navigation_page.navigate_to_recipes()

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("name", get_csv_data("data/recipe_found_by_name_data.csv"))
    def test_recipe_found_by_name(self, name):
        self.recipe_page.search_recipe_by_name(name)
        result = self.recipe_page.verify_search_by_name_success(name)
        self.test_status.mark_final("test_recipe_found_by_name", result, "Searching recipe by name was successful")

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("name", get_csv_data("data/recipe_not_found_by_name_data.csv"))
    def test_recipe_not_found_by_name(self, name):
        self.recipe_page.search_recipe_by_name(name)
        result = self.recipe_page.verify_recipe_not_found()
        self.test_status.mark_final("test_recipe_not_found_by_name", result,
                                    "No recipe was found. Searching recipe by not existing name was successful. ")

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("ingredients", get_csv_data("data/recipe_found_by_ingredients_data.csv"))
    def test_recipe_found_by_ingredients(self, ingredients):
        self.recipe_page.search_recipe_by_ingredients(ingredients)
        result = self.recipe_page.verify_search_by_ingredients_success(ingredients)
        self.test_status.mark_final("test_recipe_found_by_ingredients", result,
                                    "Searching recipe by ingredients was successful")
