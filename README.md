# Automate_Network_Login

This Software helps you in automatically Login your Internet Captive Portal.
It is built on python utilising some of its libraries like Selenium, pystray and PIL.

To use the app, download the Auto folder from the repository, it consists of two files keys.txt and Auto.exe
Type out your username and password in the keys.txt
NOTE: Make sure you you place both keys.txt and Auto.exe in the same directory before running the app.

To start the App, just launch the app by double clicking it.
You should see the app launch in the system tray.
Right click on the app symbol to find three options namely:

1. ON: When this option is selected the app tries to automate the process of logining in.
2. OFF: When this option is selected the app is temporarily suspended or halted.
3. Exit: When this option is select the app is killed or closed permanently.

To build the app from the source code follow the below steps=

Make sure you have python installed on your machine.
You can download the latest version of python from this:
https://www.python.org/downloads/

Make sure the location of the compiler is added in the PATH environment variables.

To install Selenium:
Run this command in the terminal 'pip install selenium'

Selenium uses various driver for automating different web browsers, You need to install it and again add it to the PATH environment variables.

You can download the latest version of the chromedriver from here:
https://chromedriver.chromium.org/

This application is a System Tray Application and makes use of the pystray library to implement this.

You can install pystray by running this command in your terminal: 'pip install pystray'

It also uses the PIL(Pillow) library for adding image processing capabalities to the script.

To install this again run the following command in your terminal: 'pip install Pillow'

Once all the requirements are installed, you can now run the software to automate your internet login process.

Run the script using your python interpreter.
