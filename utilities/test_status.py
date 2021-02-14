import utilities.custom_logger as cl
import logging
from traceback import print_stack
from base.function_suite import SeleniumDriverWrapper


class Status(SeleniumDriverWrapper):

    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver):
        super(Status, self).__init__(driver)
        self.result_list = []

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.result_list.append(True)
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + result_message)
                else:
                    self.result_list.append(False)
                    self.log.error("### VERIFICATION FAILED :: + " + result_message)
                    self.screen_shot(result_message)
            else:
                self.result_list.append(False)
                self.log.error("### VERIFICATION FAILED :: + " + result_message)
                self.screen_shot(result_message)
        except:
            self.result_list.append(False)
            self.log.error("### Exception Occurred !!!")
            self.screen_shot(result_message)
            print_stack()

    def mark(self, result, result_message):
        """
        Mark the result of the verification point in a test case
        """
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        """
        Mark the final result of the verification point in a test case
        This should be final test status of the test case
        """
        self.set_result(result, result_message)

        if False in self.result_list:
            self.log.error(test_name + " ### TEST FAILED")
            self.result_list.clear()
            assert False
        else:
            self.log.info(test_name + " ### TEST SUCCESSFUL")
            self.result_list.clear()
