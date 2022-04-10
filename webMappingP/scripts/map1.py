import folium 
import pandas
import os

def calculateColor(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red'



volcanoesPath = '../files/Volcanoes.csv'
worldPath = '../files/world.json'
map = folium.Map(location=(6.299672550243672, -75.55316464920128), zoom_start=8, tiles="Stamen Terrain")
if os.path.exists(volcanoesPath) and os.path.exists(worldPath):
    volcanoes = pandas.read_csv(volcanoesPath)
    lat = list(volcanoes["LAT"])
    lon = list(volcanoes["LON"])
    name = list(volcanoes["NAME"])
    elev = list(volcanoes["ELEV"])


    fgVolcanoes = folium.FeatureGroup(name="Volcanoes map")
    for lt, ln, name, el in zip(lat, lon, name, elev):
        #fg.add_child(folium.Marker(location=[lt,ln], popup=f"{name}: {str(el)} m.", icon=folium.Icon(color=calculateColor(el))))
        fgVolcanoes.add_child(folium.CircleMarker(location=[lt,ln], popup=f"{name}: {str(el)} m.",radius=8, color='grey', fill=True ,fill_color=calculateColor(el), fill_opacity=0.7))
    
    map.add_child(fgVolcanoes)

    fgPopulation = folium.FeatureGroup(name="Population 2005")
    fgPopulation.add_child(folium.GeoJson(data=(open(worldPath, 'r', encoding='utf-8-sig').read()), 
        style_function= lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 
        else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000  else 'red'}))
    
    map.add_child(fgPopulation)
    # map.add_child(folium.LayerControl())
    # map.save("../views/Map1.html")

# volcanoes=None
# map = folium.Map(location=[6.299672550243672, -75.55316464920128], zoom_start=8, tiles="Stamen Terrain")

fgHome = folium.FeatureGroup(name="Home")
for cooordinates in [[6.299672550243672, -75.55316464920128],[6.286821614691776, -75.5647436738708]]:
    fgHome.add_child(folium.Marker(location=cooordinates, popup="Juan jeje", icon=folium.Icon(color='red')))

map.add_child(fgHome)
map.add_child(folium.LayerControl())
map.save("../views/Map1.html")



