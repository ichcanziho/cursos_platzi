import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicControls(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT, "Dynamic Controls").click()

    def test_dynamic_controls(self):
        driver = self.driver
        checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox > input[type=checkbox]")
        checkbox.click()

        remove_add = driver.find_element(By.CSS_SELECTOR, "#checkbox-example > button")
        remove_add.click()

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkbox > input[type=checkbox]")))
        remove_add.click()

        enable_disable_button = driver.find_element(By.CSS_SELECTOR, "#input-example > button")
        enable_disable_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > button")))

        text_area = driver.find_element(By.CSS_SELECTOR, "#input-example > input[type=text]")
        text_area.send_keys('Platzi')

        enable_disable_button.click()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="c11_controles_dinámicos"))
