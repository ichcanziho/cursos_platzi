import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CompareProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()

    def test_account_link(self):
        WebDriverWait(self.driver, 3).until(lambda s: s.find_element(By.ID, 'select-language').get_attribute('length') == '3')

        account = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()

    def test_create_new_customer(self):  # Creacion de nuevo usuario

        # Encontrar el elemento por el texto del enlace
        self.driver.find_element(By.LINK_TEXT, 'ACCOUNT')

        # Hacer referencia a la cuenta
        my_account = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()

        # Referencia a crear una cuenta
        create_account = WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account.click()

        # Verificacion de estado de pagina web
        WebDriverWait(self.driver, 3).until(EC.title_contains('Create New Customer Account'))
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="c8_demora_implícita_explícita"))
