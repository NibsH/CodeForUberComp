import pandas as pd
import folium



df = pd.read_csv(r"C:\Users\nabal\Downloads\bus_stops.csv",sep=",")
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

coords = df[["Transport","Latitude","Longitude","District.Name"]]
city_map = folium.Map(location=[41.3851, 2.1734], zoom_start=12)

for index,row in coords.iterrows():
    mcolor = get_marker_color(row["District.Name"])
    folium.Marker(location=[row["Latitude"],row["Longitude"]],
                  popup=row["District.Name"], icon=folium.Icon(color=mcolor),).add_to(city_map)

city_map.save(r"C:\Users\nabal\Downloads\city_map2.html")