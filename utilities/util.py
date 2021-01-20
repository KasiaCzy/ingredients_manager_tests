"""
All most commonly used utilities should be implemented in this class
"""
import time
import traceback
import random, string
import utilities.custom_logger as cl
import logging


class Util(object):

    log = cl.custom_logger(logging.INFO)

    def verify_text_contains(self, actual_text, expected_text):
        """
        Verify actual text contains expected text string
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actual_text)
        self.log.info("Expected Text From Application Web UI --> :: " + expected_text)
        if expected_text.lower() in actual_text.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False