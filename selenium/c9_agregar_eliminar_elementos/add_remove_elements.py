import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By


class CompareProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()

    def test_add_remove(self):
        driver = self.driver

        add_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')

        elements_add = int(input("How many elements you want to add?: "))
        for i in range(elements_add):
            add_button.click()

        elements_removed = int(input("How many elements you want to remove?: "))

        total_elements = elements_add - elements_removed

        for i in range(elements_removed):
            try:
                button = driver.find_element(By.CLASS_NAME, "added-manually")
                button.click()
            except:
                print("You're trying to delete more elements than the existent ones")
                break

        if total_elements > 0:
            print(f"There are {total_elements} elements remaining")
        else:
            print("There are 0 elements on screen")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="c9_add_remove_elements"))
