# line-notify-bot
ゴミの日通知botです。

### Line Notifyの設定の仕方
https://qiita.com/iitenkida7/items/576a8226ba6584864d95

### APSchedulerについて
https://apscheduler.readthedocs.io/en/latest/userguide.html

requires:
```
pip install apscheduler
```

## usage
AWS EC2などで常時実行してます。
一年は無料で使えます。

```
nohup python line-bot.py
```

で継続運用できます。
messageの中を変えてカスタマイズしてください～
