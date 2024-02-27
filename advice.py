from plyer import notification
from time import sleep
import requests

data = requests.get("https://api.adviceslip.com/advice")

while True:
    if data.status_code == 200:
        notification.notify(title="Advice",message=data.json()["slip"]["advice"],app_icon= "advice.ico",timeout=10)
        sleep(7200)