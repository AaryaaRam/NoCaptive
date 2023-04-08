
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://gateway1.iiti.ac.in:8003/index.php?zone=iitiauth')
driver.implicitly_wait(30)

username = driver.find_element(By.ID,"auth_user")
password = driver.find_element(By.ID,"auth_pass")
btn = driver.find_element(By.CSS_SELECTOR,"[class='login login-submit']")

# Enter your username and password below
user = "..."   
pwrd = "..."

username.send_keys(user)
password.send_keys(pwrd)

btn.click()