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

# Subjects!!

ap = "/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[2]/bb-base-course-card"
coa = "/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[3]/bb-base-course-card"
ds = "/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[4]/bb-base-course-card"
dsl = "/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[5]/bb-base-course-card"
iml = "/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[6]/bb-base-course-card"
jp = "/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[7]/bb-base-course-card"
jpl = "/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[8]/bb-base-course-card"
lsm = "/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[9]/bb-base-course-card"
ot = "/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[10]/bb-base-course-card"
otb = "/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[11]/bb-base-course-card"
se = "/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[12]/bb-base-course-card"
sel = "/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[13]/bb-base-course-card"

"""
0 - Aptitude
1- COA
2 - DS
3 - DS Lab
4 - IM&L
5 - Java Programming
6 - Java Programming Lab
7 - LSM
8 - OT
9 - OTB
10 - SE
11 - SE Lab
"""

def switch(m):
    driver.switch_to_window(driver.window_handles[m])

def leave_session():
    # switch(1)
    status = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/span[1]/div[1]/button')
    status.click()
    print('Status clicked...(Blackboard)')
    time.sleep(2)
    leave = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/span[1]/div[2]/ul[1]/li[2]/button')
    leave.click()
    print('Clicked Leave...(Blackboard)')
    time.sleep(3)
    submit = driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[2]/button[2]')
    submit.click()
    print('Clicked Skip...(Blackboard)')
    time.sleep(8)
    driver.close()
    print('Left the session...(Blackboard)')
    print('Closed second tab...(Blackboard)')
    switch(0)
    print('Switched to first tab...(Blackboard)')
    time.sleep(5)

