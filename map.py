import folium
import pandas
map = folium.Map(location=[38,-99], zoom_start=6)
fg = folium.FeatureGroup(name="My Map")

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev= list(data["ELEV"])
name = list(data["NAME"])

def elevation_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[38,-99], zoom_start=6)

fgv = folium.FeatureGroup(name="Volcanos")

for lt , ln , el ,nm in zip(lat,lon,elev,name):
    fgv.add_child(folium.CircleMarker(location=[lt, ln],radius = 6, popup=((str(el)),nm) ,fill_color = elevation_producer(el),color = "grey",fill_opacity = 0.7, icon = folium.Icon(color = elevation_producer(el))))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data= open('115 world.json','r',encoding = 'utf-8-sig').read(),
style_function =lambda x: {'fillColor' : "green" if x['properties']['POP2005']< 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())


map.save("Map1.html")
