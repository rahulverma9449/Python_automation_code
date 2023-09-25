import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MatrixAdmin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()

    def test_data_pipeline(self):
        driver = self.driver
        driver.get('https://10.78.49.103')
        driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

