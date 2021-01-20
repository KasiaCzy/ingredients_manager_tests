from pages.ingredients.add_base_ingredient import AddBaseIngredientPage
from pages.home.navigation_page import NavigationPage
from utilities.test_status import Status
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import get_csv_data


@pytest.mark.usefixtures("one_time_set_up", "set_up")
@ddt
class AddBaseIngredientTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_set_up(self, one_time_set_up):
        self.ingredient_page = AddBaseIngredientPage(self.driver)
        self.test_status = Status(self.driver)
        self.navigation_page = NavigationPage(self.driver)

    def setUp(self):
        self.navigation_page.navigate_to_keep_track()

    @pytest.mark.run(order=2)
    @data(*get_csv_data("add_base_ingredient_valid_data.csv"))
    @unpack
    def test_valid_add_base_ingredient(self, name, unit, category):
        self.ingredient_page.add_base_ingredient(name, unit, category)
        result_1 = self.ingredient_page.verify_keep_track_page("what ingredients you have")
        self.test_status.mark(result_1, "Page Header Verified")
        result_2 = self.ingredient_page.verify_add_base_ingredient_success('tomato')
        self.test_status.mark_final("test_valid_add_base_ingredient", result_2, "Add base ingredient was successful")

    @pytest.mark.run(order=1)
    @data(*get_csv_data("add_base_ingredient_invalid_data.csv"))
    @unpack
    def test_invalid_add_base_ingredient(self, name, unit, category):
        self.ingredient_page.add_base_ingredient(name, unit, category)
        result = self.ingredient_page.verify_add_base_ingredient_failed()
        self.test_status.mark_final("test_invalid_add_base_ingredient", result, "Add base ingredient failed")
