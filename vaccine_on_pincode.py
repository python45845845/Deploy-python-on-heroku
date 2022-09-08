from re import L
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests
from selenium.webdriver.chrome.options import Options
import os
CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
options = Options()
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"))
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument("window-size=1920x1480")
ChromeOptions.add_argument("disable-dev-shm-usage")
Driver = webdriver.Chrome(chrome_options=gChromeOptions, executable_path=ChromeDriverManager().install())
options.binary_location = GOOGLE_CHROME_BIN
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.headless = True
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
driver.get("https://glauniversity.in:8070/LeadManagement/ShowResult")
s,e = 9080060,9080070
for i in range(s,e):
    a = 'GLA2022-1'+str(i).zfill(7)
    driver.find_element(By.XPATH,"//input[contains(@id,'reg')]").send_keys(a)
    driver.find_element(By.XPATH,"//input[contains(@class,'btn')]").click()
    driver.implicitly_wait(0.025)
    try :
        s = driver.find_element(By.XPATH,"//div[normalize-space()='Sorry! Registration Number Not Found']")
        print (s.txt )
    except :
        try :
            rgnames = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/h4[1]")
            rehm = rgnames.text
            def send_msg_on_telegram(rehm):
                telegram_api_url = f"https://api.telegram.org/bot5672053615:AAGRLsunpPWBSpldtOG32Gle_C_WTfrgNYo/sendMessage?chat_id=@himnandiandu&text={rehm}{a}"
                tel_resp = requests.get(telegram_api_url)
                if tel_resp.status_code == 200:
                    print ("Notification has been sent on Telegram")
                else:
                    print ("Could not send Message")
            send_msg_on_telegram(rehm)
        except :
            pass
    driver.find_element(By.XPATH,"//input[contains(@id,'reg')]").clear()
