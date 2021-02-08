from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import time
import os


class FunctionSuite:

    log = cl.custom_logger()

    def __init__(self, driver):
        self.driver = driver

    def screen_shot(self, result_message):
        file_name = result_message + "_" + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "..\\screenshots\\"
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, screenshot_directory + file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot save to directory: " + destination_file)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

    def get_title(self):
        return self.driver.title

    def get_element(self, locator, locator_type=By.ID):
        element = None
        try:
            element = self.driver.find_element(locator_type, locator)
            self.log.info("Element Found with the locator: " + locator +
                          " and  locatorType: " + locator_type)
        except NoSuchElementException:
            self.log.warning("Element not found with the locator: " + locator + " and  locatorType: " + locator_type)
        return element

    def get_elements_list(self, locator, locator_type=By.ID):
        elements = None
        try:
            elements = self.driver.find_elements(locator_type, locator)
            self.log.info("Elements list found with the locator: " + locator +
                          " and  locatorType: " + locator_type)
        except:
            self.log.warning("Elements list not found with the locator: " + locator +
                             " and  locatorType: " + locator_type)
        return elements

    def element_click(self, locator="", locator_type=By.ID, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locator_type)
        except:
            self.log.warning("Cannot click on the element with locator: " + locator + " locatorType: " + locator_type)
            print_stack()

    def element_send_keys(self, data, locator="", locator_type=By.ID, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locator_type)
        except:
            self.log.warning("Cannot send data on the element with locator: " + locator + " locatorType: " + locator_type)
            print_stack()

    def get_element_text(self, locator="", locator_type=By.ID):
        text = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                text = element.text
                text = text.strip()
        except:
            self.log.error("Failed to get text on element ")
            print_stack()
        return text

    def element_present(self, locator="", locator_type=By.ID, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.warning("Element not found")
                return False
        except:
            self.log.warning("Element not found")
            return False

    def wait_for_element(self, locator, locator_type=By.ID, timeout=10, poll_frequency=1):
        element = None
        try:
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.error("Element not appeared on the web page")
            print_stack()
        return element

    def web_scroll(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -10000);")

        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 10000);")
