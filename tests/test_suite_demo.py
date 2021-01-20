import unittest
from tests.home.login_tests import LoginTest
from tests.recipes.search_recipe_tests import SearchRecipeTest


# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SearchRecipeTest)

allTests = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(allTests)