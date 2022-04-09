import time
from datetime import datetime as dt

hostTemp = 'hosts'
hostPath = '/private/etc/hosts'
redirect="127.0.0.1"
websiteList = ["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Working hours...")
        with open(hostPath, 'r+') as file :
            content=file.read()
            for website in websiteList:
                if website not in content:
                    file.write(f"{redirect} {website} \n")
    else:
        print("Fun hours...")
        with open(hostPath, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websiteList):
                    file.write(line)
            file.truncate()
    time.sleep(5)