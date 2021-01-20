from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import time
import os


class SeleniumDriver:

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

    def get_locator_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locator_type + " not correct/supported")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_locator_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element Found with the locator: " + locator +
                          " and  locatorType: " + locator_type)
        except NoSuchElementException:
            self.log.info("Element not found with the locator: " + locator +
                          " and  locatorType: " + locator_type)
        return element

    def get_elements_list(self, locator, locator_type="id"):
        elements = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_locator_type(locator_type)
            elements = self.driver.find_elements(by_type, locator)
            self.log.info("Elements list found with the locator: " + locator +
                          " and  locatorType: " + locator_type)
        except:
            self.log.info("Elements list not found with the locator: " + locator +
                          " and  locatorType: " + locator_type)
        return elements

    def element_click(self, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locator_type)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locator_type)
            print_stack()

    def element_send_keys(self, data, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locator_type)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator + " locatorType: " + locator_type)
            print_stack()

    def get_text(self, locator="", locator_type="id", element=None, info=""):
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.get_element(locator, locator_type)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def element_present(self, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def wait_for_element(self, locator, locator_type="id",
                         timeout=10, poll_frequency=1):
        element = None
        try:
            by_type = self.get_locator_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def web_scroll(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -10000);")

        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 10000);")
