from selenium import webdriver
from getpass import getpass
import time

# Give your chromedriver.exe path
osx = input("Enter your os (Windows/Linux): ").lower()
if osx == "Windows":
    Path = input("Enter the path to your chromedriver file: ")
    Path = Path.split("\\").join("/")
    browser = webdriver.Chrome(executable_path=r(str(Path)))
else:
    Path = input("Enter the path to your chromedriver file: ")
    browser = webdriver.Chrome(executable_path=r(str(Path)))

browser.get("https://www.codechef.com/")
username_element = browser.find_element_by_id("edit-name")

# Give your username
username_element.send_keys(input("Enter the username: "))
password_element = browser.find_element_by_id("edit-pass")

# Enter password
password_element.send_keys(getpass("Enter your password: "))
browser.find_element_by_id("edit-submit").click()

# Give the link to submission page of your problem statement
problem = input("Give your problem without spaces: ")
browser.get("https://www.codechef.com/"+problem)

# For slow internet connection
time.sleep(10)

browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()

if osx == "Windows":
    code_file = input("Give your full path to solution file: ")
    code_file = code_file.split("\\").join("/")
else:
    code_file = input("Give your full path to solution file: ")

# Link to your solution in local machine
with open(r(str(code_file)),'r') as f:
    code = f.read()

code_element = browser.find_element_by_id("edit-program")
code_element.send_keys(code)

label = str(code_file).split("\\")[-1]
label_list = ['cpp','c','py','java']


if label in label_list:
    if label == 'py':
        browser.find_element_by_xpath(
            '//*[@id="edit-language"]/option[40]').click()
    elif label == 'cpp':
        browser.find_element_by_xpath(
            '//*[@id="edit-language"]/option[11]').click()
    elif label == 'c':
        browser.find_element_by_xpath(
            '//*[@id="edit-language"]/option[5]').click()
    elif label == 'java':
        browser.find_element_by_xpath(
            '//*[@id="edit-language"]/option[21]').click()

browser.find_element_by_id("edit-submit").click()

