
""" 
Developer: aipython on [29-05-2021]
website: www.aipython.in

Sends Notifications on a Telegram channel , whenever the Vaccine(s) is available at the given PINCODE 
"""

import requests
from datetime import datetime, timedelta
import time
import pytz

tele_auth_token = "5672053615:AAGRLsunpPWBSpldtOG32Gle_C_WTfrgNYo" # Authentication token provided by Telegram bot
tel_group_id = "himnandiandu"          # Telegram group name
header = {'User-Agent': 'Chrome/84.0.4147.105 Safari/537.36'} # Header for using cowin api

def send_msg_on_telegram(msg):
    telegram_api_url = f"https://api.telegram.org/bot{tele_auth_token}/sendMessage?chat_id=@{tel_group_id}&text={'hi'}"
    tel_resp = requests.get(telegram_api_url)

    if tel_resp.status_code == 200:
        print ("Notification has been sent on Telegram")
    else:
        print ("Could not send Message")

