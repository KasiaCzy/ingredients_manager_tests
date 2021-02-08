from pages.recipes.add_recipe_page import AddRecipePage
from utilities.test_status import Status
from pages.home.navigation_page import NavigationPage
import pytest
import time
from utilities.read_data import get_csv_data


@pytest.mark.usefixtures("run_app")
class TestAddRecipe:

    @pytest.fixture(autouse=True)
    def class_set_up(self, run_app):
        self.driver = run_app
        self.recipe_page = AddRecipePage(self.driver)
        self.test_status = Status(self.driver)
        self.navigation_page = NavigationPage(self.driver)

    @pytest.fixture()
    def navigate_page(self):
        self.navigation_page.navigate_to_recipes()

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("title,link,ingredients", get_csv_data("add_recipe_valid_data.csv"))
    def test_valid_add_recipe(self, title, link, ingredients, navigate_page):
        unique_title = title+str(round(time.time()*100))
        self.recipe_page.add_recipe(unique_title, link, ingredients)
        self.test_status.mark(self.recipe_page.verify_recipes_page(), "Page Header Verified")
        result = self.recipe_page.verify_add_recipe_success(unique_title)
        self.test_status.mark_final("test_valid_add_recipe", result, "Add recipe was successful")

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("title,link,ingredients", get_csv_data("add_recipe_invalid_data.csv"))
    def test_invalid_add_recipe(self, title, link, ingredients, navigate_page):
        self.recipe_page.add_recipe(title, link, ingredients)
        result = self.recipe_page.verify_add_recipe_failed()
        self.test_status.mark_final("test_invalid_add_recipe", result, "Add recipe failed")
