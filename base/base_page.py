from base.function_suite import FunctionSuite
from traceback import print_stack
from utilities.util import Util


class BasePage(FunctionSuite):

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verify_page_title(self, page_title):
        try:
            actual_title = self.get_title()
            return self.util.verify_text_contains(actual_title, page_title)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False
