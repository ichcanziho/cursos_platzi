import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By


class DynamicElements(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT, "Disappearing Elements").click()

    def test_add_remove(self):
        driver = self.driver

        options = driver.find_elements(By.TAG_NAME, "li")
        tries = 1
        while True:
            if len(options) == 5:
                break
            else:
                tries += 1
                driver.refresh()
                options = driver.find_elements(By.TAG_NAME, "li")

        print(f'Number of tries: {tries}')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="c10_elementos_dinamicos"))
