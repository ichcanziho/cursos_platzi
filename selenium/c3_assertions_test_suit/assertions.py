import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class AssertionsTest(unittest.TestCase):

    # Ejecuta (to-do) lo necesario antes de hacer una prueba, prepara el entorno de la prueba misma
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()

    def test_search_field(self):
        self.assertTrue(self.is_element_present(how=By.NAME, what="q"))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(how=By.ID, what="select-language"))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException as variable:
            return False
        return True


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="c1_hola_mundo"))
