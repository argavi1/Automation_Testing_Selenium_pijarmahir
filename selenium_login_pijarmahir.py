import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class Login_Account(unittest.TestCase): 

    def setUp(self): 
        self.driver = driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        
    def test_1_succeed_login(self): 

        driver = self.driver

        driver.get("https://pijarmahir.id")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[4]/div[2]/a[1]/button").click()
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("argavikoto@gmail.com")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("argavikoto123")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button").click()
        time.sleep(2)
        driver.find_element_by_id("phone").send_keys("895806688542")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("argavikoto123")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button").click()
        time.sleep(2)
    
    def tearDown(self): 
        self.driver.close()

    def test_2_failed_login_unregistered_email(self): 

        driver = self.driver

        driver.get("https://pijarmahir.id")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[4]/div[2]/a[1]/button").click()
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("argavikoto111@gmail.com")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("argaviargavi")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button").click()
        time.sleep(5)
    
        self.assertIn("Email yang dimasukkan tidak terdaftar")

    def tearDown(self): 
        self.driver.close() 

    def test_3_failed_login_empty_password(self): 

        driver = self.driver

        driver.get("https://pijarmahir.id")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[4]/div[2]/a[1]/button").click()
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("argavikoto@gmail.com")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button").click()
        time.sleep(5)
    
        self.assertIn("Masukkan data terlebih dahulu")

    def tearDown(self): 
        self.driver.close()

    def test_4_failed_login_incorrect_password(self): 

        driver = self.driver

        driver.get("https://pijarmahir.id")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[4]/div[2]/a[1]/button").click()
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("argavikoto@gmail.com")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("argavikoto12")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button").click()
        time.sleep(5)
    
        self.assertIn("Password yang dimasukkan salah")

    def tearDown(self): 
        self.driver.close()

    def test_5_failed_login_empty_email(self): 

        driver = self.driver

        driver.get("https://pijarmahir.id")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[4]/div[2]/a[1]/button").click()
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("argavikoto12")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button").click()
        time.sleep(5)
    
        self.assertIn("Masukkan data terlebih dahulu")

    def tearDown(self): 
        self.driver.close()

    def test_6_failed_login_SQLI_password_field(self): 

        driver = self.driver

        driver.get("https://pijarmahir.id")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[4]/div[2]/a[1]/button").click()
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("argavikoto@gmail.com")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("SELECT")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button").click()
        time.sleep(5)
    
        self.assertIn("Password yang dimasukkan salah")

    def tearDown(self): 
        self.driver.close()

    def test_7_failed_login_SQLI_email_field(self): 

        driver = self.driver

        driver.get("https://pijarmahir.id")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[4]/div[2]/a[1]/button").click()
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("SELECT count (*) FROM Users WHERE Username=’qwert’ or 1=1 -- ’ AND Password= ‘zxcvb’")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("argavikoto123")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button").click()
        time.sleep(5)
    
        self.assertIn("Format email yang dimasukkan tidak memiliki @")

    def tearDown(self): 
        self.driver.close()

    def test_8_failed_login_invalid_domain_email(self): 

        driver = self.driver

        driver.get("https://pijarmahir.id")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[4]/div[2]/a[1]/button").click()
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("argavikoto@gmail")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("argavikoto123")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button").click()
        time.sleep(5)
    
        self.assertIn("Format email yang dimasukkan tidak memiliki @")

    def tearDown(self): 
        self.driver.close()

    def test_9_failed_login_invalid_email_adress(self): 

        driver = self.driver

        driver.get("https://pijarmahir.id")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[4]/div[2]/a[1]/button").click()
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("argavikoto@@gmail")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("argavikoto123")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button").click()
        time.sleep(5)
    
        self.assertIn("Format email tidak valid")

    def tearDown(self): 
        self.driver.close()

    def test_10_failed_login_ex_registered_password(self): 

        driver = self.driver

        driver.get("https://pijarmahir.id")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[4]/div[2]/a[1]/button").click()
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("argavikoto@gmail")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("argavikoto123")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button").click()
        time.sleep(5)
    
        self.assertIn("Password yang dimasukkan salah")

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__": 
    unittest.main()