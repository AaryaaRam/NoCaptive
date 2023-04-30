import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

trigger_switch = [True]


def switch_listener():
    while True:
        new_switch_value = input("Enter (on/off): ")
        if new_switch_value == "on":
            trigger_switch[0] = True
        elif new_switch_value == "off":
            trigger_switch[0] = False


switch_thread = threading.Thread(target=switch_listener)
switch_thread.start()

while True:
    if trigger_switch[0]:
        try:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            # chrome_options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(
                'https://gateway1.iiti.ac.in:8003/index.php?zone=iitiauth')

            driver.implicitly_wait(3)

            username = driver.find_element(By.ID, "auth_user")
            password = driver.find_element(By.ID, "auth_pass")
            btn = driver.find_element(
                By.CSS_SELECTOR, "[class='login login-submit']")

            # Enter your username and password below
            user = "cse210001065"
            pwrd = "9908119320"

            username.send_keys(user)
            password.send_keys(pwrd)

            btn.click()

        except:
            print("You are connected")

    else:
        driver.quit()
