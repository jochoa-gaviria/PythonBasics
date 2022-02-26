import requests
from bs4 import BeautifulSoup
import pandas


r = requests.get('https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/')
c = r.content
soup=BeautifulSoup(c, "html.parser")

pageNumber = soup.find_all("a", {"class":"Page"})[-1].text


propertyDataList = []
for page in range(0, int(pageNumber)*10, 10):
    propertiesPage = requests.get(f'https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s={page}.html')


    content = propertiesPage.content

    soup= BeautifulSoup(content, "html.parser")

    propertiesRows = soup.find_all("div", {"class":"propertyRow"})


    for property in propertiesRows:
        propertyData={}
        propertyData["Address"]=property.find_all("span", {"class":"propAddressCollapse"})[0].text
        try:
            propertyData["Locality"]=property.find_all("span", {"class":"propAddressCollapse"})[1].text
        except:
            propertyData["Locality"]=None
        propertyData["Price"]=property.find("h4", {"class":"propPrice"}).text.strip()
        try:
            propertyData["Beds"]=property.find("span", {"class":"infoBed"}).find("b").text
        except:
            propertyData["Beds"]=None
        try:
            propertyData["areaSize"]=property.find("span", {"class":"infoSqFt"}).find("b").text
        except:
            propertyData["areaSize"]=None
        try:
            propertyData["fullBath"]=property.find("span", {"class":"infoValueFullBath"}).find("b").text
        except:
            propertyData["fullBath"]=None
        try:
            propertyData["halfBath"]=property.find("span", {"class":"infoValueHalfBath"}).find("b").text
        except:
            propertyData["halfBath"]=None

        for columnGroup in property.find_all("div", {"class":"columnGroup"}):
            for featureGroup, featureName in zip(columnGroup.find_all("span", {"class":"featureGroup"}), columnGroup.find_all("span", {"class":"featureName"})):
                # print(featureGroup.text, featureName.text)
                if "Lot Size" in featureGroup.text:
                    propertyData["lotSize"]=featureName.text
                else:
                    propertyData["lotSize"]=None
        propertyDataList.append(propertyData)

propertyDataFrame= pandas.DataFrame(propertyDataList)
propertyDataFrame.to_csv("OutputFile.csv")

print(propertyDataFrame)