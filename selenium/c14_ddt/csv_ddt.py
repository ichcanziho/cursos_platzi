import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from ddt import ddt, data, unpack


def read_data(file_name):
    return pd.read_csv(file_name, skiprows=1).values.tolist()


@ddt
class SearchDDT(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.get('http://demo-store.seleniumacademy.com')
        driver.maximize_window()

    @data(*read_data("c14_ddt/testdata.csv"))
    @unpack
    def test_search(self, search_value, expected_count):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements(By.XPATH, '//h2[@class= "product-name"]/a')

        expected_count = int(expected_count)
        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element(By.CLASS_NAME, 'note-msg').text
            self.assertEqual('Your search returns no results.', message)
        print(f'Found {len(products)} products')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="c14_ddt"))

