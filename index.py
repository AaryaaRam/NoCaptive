import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


os.environ["PATH"]+=r"C:\DRIVERS\SeleniumDrivers"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://gateway1.iiti.ac.in:8003/index.php?zone=iitiauth')
driver.implicitly_wait(30)
# username = driver.find_element_by_id('auth_user')
username = By.CLASS_NAME("auth_user")
# password = driver.find_element_by_id('auth_pass')
password = By.CLASS_NAME("auth_pass")
 
username.send_keys("cse210001065@iiti.ac.in")
password.send_keys("9908119320")
