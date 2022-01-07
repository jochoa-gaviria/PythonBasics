## Import time module ##
import time
import os
import pandas

for i in range(3):
    if os.path.exists("../Files/supermarkets/fruits.txt"):   ##To check if the file (path) exists.
        with open("../Files/supermarkets/fruits.txt") as file:
            print(file.read())
            time.sleep(4)
    else:
        print("File does not exists")
## Import time module ##


### import sys
### import os
### sys.builtin_module_names >> to see the modules wrotes in C languaje
### sys.prefix >> to see the path of modules wrotes in Python languaje


### How to install another libraries third-party using pip
### sudo apt install python3-pip

for i in range(3):
    if os.path.exists("../Files/csv/temps_today.csv"):   ##To check if the file (path) exists.
        data = pandas.read_csv("../Files/csv/temps_today.csv")
        print(data.mean()['st1'])
    else:
        print("File does not exists")