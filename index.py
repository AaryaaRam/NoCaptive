import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pystray
import PIL.Image
image = PIL.Image.open("icon.png")

trigger_switch = True
connected = False


def exit_app(icon, item):
    global trigger_switch, connected
    trigger_switch = False
    icon.stop()


def login():
    global trigger_switch, connected
    while (trigger_switch) and (not connected):
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

            driver.quit()
        except:
            print("You are connected")
            connected = True


def switch_listener(icon, item):
    global trigger_switch
    global connected
    print("SWITCH : ")
    print(item)
    print(icon)
    while True:
        if str(item) == "ON":
            trigger_switch = True
            connected = False
            print("LOGIN : ")
            # check_connected()
            if not connected:
                login()
        elif str(item) == "OFF":
            trigger_switch = False
            break
        # elsif new


icon = pystray.Icon("temp", image, menu=pystray.Menu(
    pystray.MenuItem("ON", switch_listener),
    pystray.MenuItem("OFF", switch_listener),
    pystray.MenuItem("EXIT", exit_app)
))

icon.run()

# switch_thread = threading.Thread(target=switch_listener)
# switch_thread.start()

# def check_connected():
#     try:
#         chrome_options = Options()
#         chrome_options.add_argument('--headless')
#         # chrome_options.add_experimental_option("detach", True)
#         driver = webdriver.Chrome(options=chrome_options)
#         driver.get(
#             'https://gateway1.iiti.ac.in:8003/index.php?zone=iitiauth')

#         driver.implicitly_wait(3)

#         username = driver.find_element(By.ID, "auth_user")
#         connected = False
#     except:
#         connected = True
