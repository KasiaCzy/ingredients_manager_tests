from pages.ingredients.add_base_ingredient_page import AddBaseIngredientPage
from pages.home.navigation_page import NavigationPage
from utilities.test_status import Status
import pytest
import time
from utilities.read_data import get_csv_data


@pytest.mark.usefixtures("run_app")
class TestAddBaseIngredient:

    @pytest.fixture(autouse=True)
    def class_set_up(self, run_app):
        self.driver = run_app
        self.ingredient_page = AddBaseIngredientPage(self.driver)
        self.test_status = Status(self.driver)
        self.navigation_page = NavigationPage(self.driver)

    @pytest.fixture()
    def navigate_page(self):
        self.navigation_page.navigate_to_keep_track()

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("name,unit,category", get_csv_data("add_base_ingredient_valid_data.csv"))
    def test_valid_add_base_ingredient(self, name, unit, category, navigate_page):
        unique_name = name+str(round(time.time()*100))
        self.ingredient_page.add_base_ingredient(unique_name, unit, category)
        self.test_status.mark(self.ingredient_page.verify_keep_track_page(), "Page Header Verified")
        result = self.ingredient_page.verify_add_base_ingredient_success(unique_name)
        self.test_status.mark_final("test_valid_add_base_ingredient", result, "Add base ingredient was successful")

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("name,unit,category", get_csv_data("add_base_ingredient_invalid_data.csv"))
    def test_invalid_add_base_ingredient(self, name, unit, category, navigate_page):
        self.ingredient_page.add_base_ingredient(name, unit, category)
        result = self.ingredient_page.verify_add_base_ingredient_failed()
        self.test_status.mark_final("test_invalid_add_base_ingredient", result, "Add base ingredient failed")
