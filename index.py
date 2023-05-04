import os
import sys
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pystray
import PIL.Image
import time
import re

file = open("keys.txt", "r")
keys = re.findall(r'"(.+?)"', file.read())
# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")

#     return os.path.join(base_path, relative_path)


# image = PIL.Image.open(resource_path("./icon.png"))
image = PIL.Image.open('icon.png')

trigger_switch = [False]


def login():
    while (True):
        if (trigger_switch[0] == False):
            while (not trigger_switch[0]):
                time.sleep(5)
        if (trigger_switch[0] == "Exit"):
            return
        if (trigger_switch[0] == True):
            try:
                chrome_options = Options()
                chrome_options.add_argument('--headless')
                # chrome_options.add_experimental_option("detach", True)
                driver = webdriver.Chrome(options=chrome_options)
                driver.get(
                    'https://gateway1.iiti.ac.in:8003/index.php?zone=iitiauth')

                driver.implicitly_wait(5)

                username = driver.find_element(By.ID, "auth_user")
                password = driver.find_element(By.ID, "auth_pass")
                btn = driver.find_element(
                    By.CSS_SELECTOR, "[class='login login-submit']")

                user = keys[0]
                pwrd = keys[1]

                username.send_keys(user)
                password.send_keys(pwrd)
                btn.click()

                driver.quit()
            except Exception as e:
                print("e")


switch_thread = threading.Thread(target=login)
switch_thread.start()


def switch_listener(icon, item):
    if str(item) == "ON":
        trigger_switch[0] = True
    elif str(item) == "OFF":
        trigger_switch[0] = False
    elif str(item) == "EXIT":
        trigger_switch[0] = "Exit"
        icon.stop()


icon = pystray.Icon("temp", image, menu=pystray.Menu(
    pystray.MenuItem("ON", switch_listener),
    pystray.MenuItem("OFF", switch_listener),
    pystray.MenuItem("EXIT", switch_listener)
))

icon.run()
