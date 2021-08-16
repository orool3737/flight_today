from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import datetime
import requests
from bs4 import BeautifulSoup
import telegram
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cralwer_flight_hiair_today import exract_flight_hiair_today

first_content = exract_flight_hiair_monday('16','0')
 
bot = telegram.Bot(token=os.environ.get('telegram_token'))
chat_id = 1491027495 #bot.getUpdates()[-1].message.chat.id

bot.sendMessage(chat_id=chat_id, text=total_content_clean)
