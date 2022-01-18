import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class Registration_Account(unittest.TestCase): 

    def setUp(self): 
        self.driver = driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        
    def test_1_succeed_registration(self): 

        driver = self.driver

        driver.get("https://pijarmahir.id")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[4]/div[2]/a[2]/button").click()
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("sammi2009@booksp.site")
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button').click()
        time.sleep(300)
        driver.find_element_by_id("fullname").send_keys("argavi koto")
        time.sleep(3)
        driver.find_element_by_id("phone").send_keys("895806688542")
        time.sleep(3)
        driver.find_element_by_id("password").send_keys("argavikoto123")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button").click()
        time.sleep(2)
    
    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()