import time
from datetime import datetime as dt
hostPath = 'etc/hosts'
redirect="127.0.0.1"
websiteList = ["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours...")
    else:
        print("Fun hours...")
    time.sleep(5)