## pip3 install request
## pip3 install bs4

import requests
from bs4 import BeautifulSoup

r = requests.get('https://pythonizing.github.io/data/example.html')
content=r.content

soup=BeautifulSoup(content,'html.parser')

# print(soup.prettify())

all=soup.find_all("div", {"class":"cities"})

cities = []
for city in all:
    cities.append(city.find_all("h2")[0].text)

print(cities)