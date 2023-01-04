import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class HelloWord(unittest.TestCase):

    # Ejecuta (to-do) lo necesario antes de hacer una prueba, prepara el entorno de la prueba misma
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.implicitly_wait(10)

    # Caso de prueba, lo que quiero automatizar
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.fahorro.com/aspirina-protec-100-mg-oral-28-tabletas.html')

    def test_wikipedia(self):
        driver = self.driver
        driver.get('https://www.wikipedia.org')

    # Qué hacer cuando to-do termina?, en este caso cerramos las ventanas del navegador para no consumir recursos
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="c1_hola_mundo"))
