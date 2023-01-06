import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By


class DynamicElements(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT, "Typos").click()

    def test_dynamic_controls(self):
        driver = self.driver
        typo_text = driver.find_element(By.XPATH, '//*[@id="content"]/div/p[2]').text
        tries = 1
        max_tries = 10
        error_flag = False
        while typo_text != "Sometimes you'll see a typo, other times you won't.":
            typo_text = driver.find_element(By.XPATH, '//*[@id="content"]/div/p[2]').text
            self.driver.refresh()
            if max_tries:
                error_flag = True
                break
            tries += 1
        self.assertFalse(error_flag)
        print(f"It took {tries} tries to be found")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="c12_typos"))
