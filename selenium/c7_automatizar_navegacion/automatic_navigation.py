import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class CompareProducts(unittest.TestCase):

    # Ejecuta (to-do) lo necesario antes de hacer una prueba, prepara el entorno de la prueba misma
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.get("https://google.com/")
        driver.maximize_window()

    def test_browser_navigation(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()

        search_field.send_keys('platzi')
        search_field.submit()

        driver.back()
        sleep(3)
        driver.forward()
        sleep(3)
        driver.refresh()
        sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="c7_automatizar_navegacion"))
