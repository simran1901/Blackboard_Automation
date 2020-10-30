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

try:
    consent = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div/div/div[2]/button")
    consent.click()
    print('Accepted privacy and consent...(Blackboard)')
except NoSuchElementException:
    pass

time.sleep(3)

# Login functions
def bb_login():
    username = driver.find_element_by_name("user_id")
    username.clear()
    username.send_keys('<yourUsername>')
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys('<yourPassword>')
    login_button = driver.find_element_by_id("entry-login")
    login_button.click()

def insta_login():
    igname = second_driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
    igname.clear()
    igname.send_keys('<yourUsername>')
    igpass = second_driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
    igpass.clear()
    igpass.send_keys('<yourPassword>')
    login = second_driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
    login.click()

bb_login()
print('Logged into Blackboard...')
insta_login()
print('Logged into Instagram...')
time.sleep(10)

not_now = second_driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
not_now.click()
print('Clicked \'Not Now\'...(Instagram)')
time.sleep(5)
direct_message = second_driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')
direct_message.click()
print('Clicked \'Direct Message\'...(Instagram)')

time.sleep(5)

