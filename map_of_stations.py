import pandas as pd
import folium

df = pd.read_csv("transports.csv",sep=",")

def get_marker_color(transport) -> str:
    if transport == "Underground":
        return "blue"
    elif transport == "Railway (FGC)":
        return "green"
    elif transport == "Tram":
        return "orange"
    else:
        return "red"

coords = df[["Transport","Latitude","Longitude","Station"]]
city_map = folium.Map(location=[41.3851, 2.1734], zoom_start=12)

for index,row in coords.iterrows():
    mcolor = get_marker_color(row["Transport"])
    folium.Marker(location=[row["Latitude"],row["Longitude"]],
                  popup=row["Station"], icon=folium.Icon(color=mcolor),).add_to(city_map)

city_map.save("city_map.html")