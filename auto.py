from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

profile_link = "https://www.linkedin.com/in/mayu-yamakawa/" # in the future, this will become a list of links

options = Options()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
driver_path = '/Users/linhvu/Desktop/chromedriver-mac-arm64/chromedriver'
service = Service(executable_path=driver_path)
drvr = webdriver.Chrome(options = options, service = service)

drvr.get("https://www.linkedin.com/login")
## login
username = drvr.find_element(By.ID, "username")
password = drvr.find_element(By.ID, "password")
with open("user_input.json") as f:
    json_file = json.load(f)
user_input = json_file["username"]
user_password = json_file["password"]
username.send_keys(user_input)
password.send_keys(user_password)
password.send_keys(Keys.RETURN)
# visit profile
drvr.get(profile_link)
# connect
try:
    time.sleep(3)
    # @aria-label='Invite Mayu Yamakawa to connect'
    # TODO: Futher inspect the button to see which tag to click on
    # retry @aria-label above if possible.
    connect_button = drvr.find_element(By.XPATH, ".//button[@id='ember113']") # this is the specific
    # button for Mayu, other people will have different id
    # print(connect_button)
    # print("Connect button found")
    
    connect_button.click()
    # the code above should be able to click on the connect button and shows the 
    # pop up window to add a note or without a note
    print("button clicked")
    # handle add a note, send without a note
    # send_without_note = drvr.find_element(By.XPATH, "//button[@aria-label='Send without a note']")
    time.sleep(5)
    # send_without_note.click()
    # print("Connection sent")
except Exception as e:
    print("Connect button not found or not clickable:", e)
    
# TODO: Other cases scnearios where we have to click on more to add a person