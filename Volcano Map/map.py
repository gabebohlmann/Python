import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation = list(data["ELEV"])

def markerColor(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location = [38.58, -99.09], zoom_start = 6, titles = "Stamen Terrain")

volcanoes_feature_group = folium.FeatureGroup(name = "Volcanoes")

for lat, lon, elev in zip(latitude, longitude, elevation):
    volcanoes_feature_group.add_child(folium.CircleMarker(location = [lat, lon], radius = 5, popup = str(elev),
        fill_color = markerColor(elev), color = 'grey', fill_opacity = 0.7))

population_feature_group = folium.FeatureGroup(name="Population")

population_feature_group.add_child(folium.GeoJson(data = open('world.json', 'r', encoding='utf-8-sig').read(), 
    style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
        else 'orange' if 10000000 <= x['properties']['POP2005'] < 200000000
        else 'red'}))

map.add_child(volcanoes_feature_group)
map.add_child(population_feature_group)
map.add_child(folium.LayerControl())

map.save("Map.html")