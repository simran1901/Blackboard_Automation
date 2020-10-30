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