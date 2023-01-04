import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class HelloWord(unittest.TestCase):

    # Ejecuta to-do lo necesario antes de hacer una prueba, prepara el entorno de la prueba misma
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()

    # Caso de prueba, lo que quiero automatizar
    def test_serch_text_field(self):
        driver = self.driver
        search_field = driver.find_element(By.ID, "search")

    def test_search_text_field_by_name(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, "q")

    def test_search_text_field_by_class_name(self):
        driver = self.driver
        search_field = driver.find_element(By.CLASS_NAME, "input-text")

    def test_search_button_enable(self):
        driver = self.driver
        button = driver.find_element(By.CLASS_NAME, "button")

    def test_count_of_promo_banner_images(self):
        driver = self.driver
        banner_list = driver.find_element(By.CLASS_NAME, "promos")
        banners = banner_list.find_elements(By.TAG_NAME, 'img')
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        driver = self.driver
        vip_promo = driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')

    def test_shopping_cart(self):
        driver = self.driver
        # se encuentra dentro de un div class header-mini cart a su vez dentro de un span con class icon
        shopping_cart_icon = driver.find_element(By.CSS_SELECTOR, 'div.header-minicart span.icon')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="c2_find_element"))
