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

def isPolling():
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/div[1]/span/button')
        temp = int(span.strip())
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/div[1]/div/div/div/ul/li['+str(temp)+']/button')
        print('Going for polling...(Blackboard)')
        return True
    except (NoSuchElementException, ValueError):
        print('Polling is not applicable...(Blackboard)')
        return False

def isChat():
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[3]/section/section/bb-chat-input/div/div/textarea')
        return True
    except NoSuchElementException:
        return False

def del_ch():
    clear_chat = second_driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[3]/button')
    clear_chat.click()
    delete_chat = second_driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div[1]/button')
    delete_chat.click()
    confirm_delete = second_driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/button[1]')
    confirm_delete.click()
    print('Deleted chat...(Instagram)')

def start_session(n, end):
    """It starts a new session"""
    global sessions
    n = driver.find_element_by_xpath(n)
    n.click()
    time.sleep(10)

    while True:
        try:
            session_list = driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/div[3]/aside/div[6]/div[2]/div[2]/div/div/button/span')
            print('Got session list...(Blackboard)')
            time.sleep(5)
            try:
                session_list.click()
            except ElementNotInteractableException:
                continue
            break
        except NoSuchElementException:
            time.sleep(5)
    time.sleep(5)
    try:
        li = driver.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/div[3]/aside/div[6]/div[2]/div[2]/div/div/ul/li[3]")
        print('3rd session is active...(Blackboard)')
    except NoSuchElementException:
        try:
            li = driver.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/div[3]/aside/div[6]/div[2]/div[2]/div/div/ul/li[2]")
            print('2nd session is active...(Blackboard)')
        except NoSuchElementException:
            li = driver.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/div[3]/aside/div[6]/div[2]/div[2]/div/div/ul/li[1]")
            print('1st session is active...(Blackboard)')
    li.click()
    print('Choosing a session...(Blackboard)')
    print('Session number: '+ str(sessions) + '...(Blackboard)')
    time.sleep(5)
    driver.close()
    switch(1)
    print('Switched to second tab...(Blackboard)')
    # ***** Optional audio and video checks *****
    # audiocheck = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div/div[2]/button')
    # audiocheck.click()
    # time.sleep(30)
    # videocheck = driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/div/div/div[3]/div/button')
    # videocheck.click()
    while True:
        try:
            cross = driver.find_element_by_xpath('/html/body/div[5]/div/button')
            break
        except NoSuchElementException:
            time.sleep(10)
    cross.click()
    print('Cancelled audio and video checks...(Blackboard)')
    
    if sessions == 0:
        time.sleep(20)
        later = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[4]/button')
        later.click()
        print('Clicked Later...(Blackboard)')
        time.sleep(2)
        nav = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/bb-tutorial-dialog/div/div[2]/button')
        nav.click()
        print('Clicked Close...(Blackboard)')
    
    time.sleep(10)
    chat_button = driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/bb-panel-open-control/div/button[1]')
    chat_button.click()
    print('Clicked chat field...(Blackboard)')
    time.sleep(5)
    everyone = driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[3]/section/div/div/ul/li/ul/li/bb-channel-list-item/button')
    everyone.click()
    print('Choosing Everyone...(Blackboard)')
    try:
        close = driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[3]/section/section/bb-chat-input/div/bb-guidance-dialog/div/button')
        close.click()
        print('Clicking Close...(Blackboard)')
    except NoSuchElementException:
        print('Chat is off...(Blackboard)')

    if datetime.now()<end:

        send_message = second_driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/button')
        send_message.click()
        print('Send Message has been clicked...(Instagram)')
        name_field = second_driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input')
        name_field.clear()
        name_field.send_keys('<classmate_username>')
        print('Entering name...(Instagram)')
        time.sleep(2)
        select = second_driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[2]/div[1]/div/div[3]/button')
        select.click()
        print('Clicking Select...(Instagram)')
        time.sleep(3)
        next_key = second_driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/div/button')
        next_key.click()
        print('Clicking Next...(Instagram)')
        time.sleep(10)

        # Clear chat
        del_ch()
        
        time.sleep(2)
        text_area = second_driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        text_area.clear()
        text_area.send_keys('I should start answering now.')
        print('Typed a message...(Instagram)')
        send_key = second_driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
        send_key.click()
        print('Sent a message...(Instagram)')
        time.sleep(5)
        msgno = 3
        
        while datetime.now()<end:
            
            while datetime.now()<end:
                
                try:
                    msgloc = '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div['+str(msgno)+']/div[2]/div/div/div/div/div/div/div/div/span'
                    span = (second_driver.find_element_by_xpath(msgloc)).text
                    msgno += 1
                    break

                except NoSuchElementException:
                    time.sleep(10)
           
            # switch(1)
            time.sleep(5)
            if isPolling():
                pollopt = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/div[1]/div/div/div/ul/li['+span.strip()+']/button')
                pollopt.click()
            elif isChat():
                print('Going for chat...(Blackboard)')
                chat_area = driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[3]/section/section/bb-chat-input/div/div/textarea')
                chat_area.clear()
                chat_area.send_keys(span)
                chat_area.send_keys(Keys.ENTER)
            time.sleep(2)
            # switch(2)

        try:
            del_ch()

        except NoSuchElementException:
            pass
        
    sessions += 1
    leave_session()
