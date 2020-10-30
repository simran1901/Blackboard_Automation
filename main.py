from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time
from datetime import datetime

# To count the number of sessions
global sessions
sessions = 0
# To get the text from messages
span = ""

# Set Chrome options
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument('--no-sandbox')
opt.add_argument('--ignore-certificate-errors-spki-list')
opt.add_argument('--ignore-ssl-errors')
# opt.add_argument("--incognito")
opt.add_experimental_option("prefs", {
                                        "profile.default_content_setting_values.media_stream_mic": 1,
                                        "profile.default_content_setting_values.media_stream_camera": 1,
                                        "profile.default_content_setting_values.geolocation": 2,
                                        "profile.default_content_setting_values.notifications": 2,
})
opt.add_argument("--disable-extensions")

# DRIVER_PATH = "C:\\Users\\Makhijani's\\Downloads\\chromedriver_win32\\chromedriver.exe"

# Open browser
second_driver = webdriver.Chrome(options=opt)
print('Opened up a browser for instagram...')
driver = webdriver.Chrome(options=opt)
print('Opened up a browser for Blackboard...')

# Get the sites
driver.get("https://cuchd.blackboard.com/")
second_driver.get('https://www.instagram.com')

