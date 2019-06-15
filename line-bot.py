# coding: UTF-8

import requests
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

class LINENotifyBot:
    API_URL = 'https://notify-api.line.me/api/notify'
    def __init__(self, access_token):
        self.__headers = {'Authorization': 'Bearer ' + access_token}

    def send(
            self, message,
            image=None, sticker_package_id=None, sticker_id=None,
            ):
        payload = {
            'message': message,
            'stickerPackageId': sticker_package_id,
            'stickerId': sticker_id,
            }
        files = {}
        if image != None:
            files = {'imageFile': open(image, 'rb')}
        r = requests.post(
            LINENotifyBot.API_URL,
            headers=self.__headers,
            data=payload,
            files=files,
            verify=False
            )

def job():
  print("starting job")
  weekday = datetime.date.today().weekday()
  token = "YOUR ACCESS TOKEN"
  bot = LINENotifyBot(access_token=token)
  
  if weekday == 0:
    #月曜
    message = "今日はプラゴミの日です。"
    bot.send(message=message)
  elif weekday == 1:
    # 火曜
    message = "今日は燃えるゴミの日です。"
    bot.send(message=message)
  elif weekday == 2:
    # 水曜
    message = "今日は"
    bot.send(message=message)  
  elif weekday == 4:
    # 金曜
    message = "今日は燃えるゴミとダンボールの日です。"
    bot.send(message=message)
  elif weekday == 5:
    message = "今日はビンカンペットボトルの日です"
    bot.send(message=message)
  else:
    pass

# Schedules job_function to be run every 7AM.
sched  = BlockingScheduler()
sched.add_job(job, "cron", hour="7")

sched.start()

