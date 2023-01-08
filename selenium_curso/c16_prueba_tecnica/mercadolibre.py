import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class MercadoLibreTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.get("https://mercadolibre.com/")
        driver.maximize_window()

    def test_compra_pantalla(self):

        driver = self.driver
        driver.find_element(By.ID, "MX").click()
        query = driver.find_element(By.CLASS_NAME, "nav-search-input")
        query.click()
        query.clear()
        query.send_keys("pantalla 43 pulgadas")
        query.submit()
        sleep(3)
        price = driver.find_element(By.CLASS_NAME, 'andes-dropdown__trigger')
        price.click()
        price = price.find_element(By.XPATH, '//*[@id="andes-dropdown-más-relevantes-list-option-price_desc"]/div/div/span')
        price.click()
        sleep(3)
        articles = []
        prices = []
        for i in range(5):
            article_dir = f'/html/body/main/div/div[2]/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2'
            price_dir = f'/html/body/main/div/div[2]/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]'
            try:
                article_name = driver.find_element(By.XPATH, article_dir).text
                article_price = driver.find_element(By.XPATH, price_dir).text
                print(article_name, article_price)
                articles.append(article_name)
                prices.append(article_price)
            except:
                pass
        print(articles)
        print(prices)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="c16_prueba_tecnica"))
