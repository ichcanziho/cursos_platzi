import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CompareProducts(unittest.TestCase):

    # Ejecuta (to-do) lo necesario antes de hacer una prueba, prepara el entorno de la prueba misma
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()

    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        # como buena práctica se recomienda limpiar los campos
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

        driver.find_element(By.CLASS_NAME, 'link-compare').click()
        driver.find_element(By.LINK_TEXT, 'Clear All').click()

        # creamos una variable para interactuar con el pop-up
        alert = driver.switch_to.alert
        # vamos a extraer el texto que muestra
        alert_text = alert.text

        # vamos a verificar el texto de la alerta
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

        alert.accept()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="c6_manejo_alert_pop_up"))
