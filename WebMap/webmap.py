import folium
import pandas

data = pandas.read_csv("data.csv")
latitude = list(data["Latitude"]) 
longitude = list(data["Longitude"])
name = list(data["Restaurant Name"]) 
locality = list(data["Locality"])
avg_cost = list(data["Average Cost for two"])

def color_code(avg_cost):
    if avg_cost<500:
        return 'lightgreen' 
    elif avg_cost<1000 and avg_cost>=500:
        return 'green'
    elif avg_cost<1500 and avg_cost>=1000:
        return 'orange'
    else:
        return 'red'

my_map = folium.Map(location = [12.92,77.5],tiles = "Stamen Terrain")
 
fg_r = folium.FeatureGroup(name= "Restaurants") # feature group of markers
for lat,lon,nm,loc,avg in zip(latitude,longitude,name,locality,avg_cost):
    fg_r.add_child(folium.Marker(location = [lat,lon], popup=nm+"-"+loc, icon = folium.Icon(color= color_code(avg))))
# Note- popup parameter only takes a string

fg_p = folium.FeatureGroup(name= "Population")
fg_p.add_child(folium.GeoJson(data= open("world.json", 'r', encoding= "utf-8-sig").read(),
style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] <20000000 else 'red'}))
#add geojson polygon layer

my_map.add_child(fg_r) # add feature group as child
my_map.add_child(fg_p) 
my_map.add_child(folium.LayerControl())

my_map.save("Bengaluru.html")
