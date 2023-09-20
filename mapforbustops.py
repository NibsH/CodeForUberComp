import geopandas as gpd
import folium
import pandas as pd


gdf = gpd.read_file(r"C:\Users\nabal\Downloads\shapefiles_barcelona_distrito.shp")


barcelona_map = folium.Map(location=[41.3851, 2.1734], zoom_start=12)



import geopandas as gpd
import folium
import pandas as pd


gdf = gpd.read_file(r"C:\Users\nabal\Downloads\shapefiles_barcelona_distrito.shp")


barcelona_map = folium.Map(location=[41.3851, 2.1734], zoom_start=12)


folium.GeoJson(gdf,
               style_function=lambda feature: {
                   'fillOpacity': 0.4,  
                   'color': 'black',     
                   'weight': 2           
               }).add_to(barcelona_map)


df = pd.read_csv(r"C:\Users\nabal\Downloads\bus_stops.csv", sep=",")
df = df.sort_values(by=['District.Name'])

def get_marker_color(district) -> str:
    if district == "Ciutat Vella":
        return "blue"
    elif district == "Eixample":
        return "green"
    elif district == "Sants-Montjuïc":
        return "orange"
    elif district == 'Les Corts':
        return "red"
    elif district == 'Sarrià-Sant Gervasi':
        return "purple"
    elif district == 'Gràcia':
        return "brown"
    elif district == 'Horta-Guinardó':
        return "pink"
    elif district == 'Nou Barris':
        return "gray"
    elif district == 'Sant Andreu':
        return "black"
    else:
        return 'beige'

coords = df[["Transport", "Latitude", "Longitude", "District.Name"]]


for index, row in coords.iterrows():
    mcolor = get_marker_color(row["District.Name"])
    folium.Marker(location=[row["Latitude"], row["Longitude"]],
                  popup=row["District.Name"], icon=folium.Icon(color=mcolor)).add_to(barcelona_map)




barcelona_map.save(r"C:\Users\nabal\Downloads\combined_map.html")



