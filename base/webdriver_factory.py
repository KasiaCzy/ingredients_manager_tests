from selenium import webdriver


class WebDriverFactory:
    def __init__(self, browser):
        self.browser = browser

    def get_webdriver_instance(self):
        base_url = 'http://127.0.0.1:8000/'
        if self.browser == "iexplorer":
            driver = webdriver.Ie(executable_path='drivers\\IEDriverServer.exe')
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path='drivers\\geckodriver.exe')
        elif self.browser == "chrome":
            driver = webdriver.Chrome(executable_path='drivers\\chromedriver.exe')
            driver.set_window_size(1440, 900)
        else:
            driver = webdriver.Firefox(executable_path='drivers\\geckodriver.exe')
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_url)
        return driver
