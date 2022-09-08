import requests
tele_auth_token = "5672053615:AAGRLsunpPWBSpldtOG32Gle_C_WTfrgNYo" # Authentication token provided by Telegram bot
tel_group_id = "himnandiandu"  
msg = f"msg reci atubu "
def send_msg_on_telegram(msg):
    telegram_api_url = f"https://api.telegram.org/bot{tele_auth_token}/sendMessage?chat_id=@{tel_group_id}&text={msg}"
    tel_resp = requests.get(telegram_api_url)

    if tel_resp.status_code == 200:
        print ("Notification has been sent on Telegram")
    else:
        print ("Could not send Message")

send_msg_on_telegram(msg)


