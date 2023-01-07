import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


class SortTables(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT, "Sortable Data Tables").click()

    def test_sort_tables(self):
        driver = self.driver
        header = driver.find_elements(By.XPATH, '//*[@id="table1"]/thead/tr/th')
        header_text = [cell.text for cell in header[:-1]]
        body_table = driver.find_elements(By.XPATH, '//*[@id="table1"]/tbody/tr')
        table = []
        for row in body_table:
            values = row.find_elements(By.XPATH, "td")
            values = [cell.text for cell in values[:-1]]
            table.append(values)
        table_df = pd.DataFrame(data=table, columns=header_text)
        print(table_df)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="c13_tables"))
