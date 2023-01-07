import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class LanguageOptions(unittest.TestCase):

    # Ejecuta (to-do) lo necesario antes de hacer una prueba, prepara el entorno de la prueba misma
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()

    def test_select_language(self):
        # el orden respeta como aparecen en la página
        exposed_options = ['English', 'French', 'German']
        # para almacenar las opciones que elijamos
        active_options = []
        # para acceder a las opciones del dropdown SELECT fue un import especial de WebDriver -> ver imports
        select_language = Select(self.driver.find_element(By.ID, 'select-language'))
        # para comprobar que si esté la cantidad de opciones correcta
        # 'options' permite ingresar directamente a las opciones del dropdown
        self.assertEqual(3, len(select_language.options))

        for option in select_language.options:
            active_options.append(option.text)

        # verifico que la lista de opciones disponibles y activas sean indénticas
        self.assertListEqual(exposed_options, active_options)

        # vamos a verificar la palabra "English" sea la primera opción seleccionada del dropdown
        self.assertEqual('English', select_language.first_selected_option.text)

        # seleccionamos "German" por el texto visible
        select_language.select_by_visible_text('German')

        # verificamos que el sitio cambio a Alemán
        # preguntamos a selenium_curso si la url del sitio contiene esas palabras
        self.assertTrue('store=german' in self.driver.current_url)

        select_language = Select(self.driver.find_element(By.ID, 'select-language'))
        select_language.select_by_index(0)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="c5_manejo_dropdown_lista"))
