import geopandas as gpd
import folium

gdf = gpd.read_file(r"C:\Users\nabal\Downloads\shapefiles_barcelona_distrito.shp")


barcelona_map = folium.Map(location=[41.3851, 2.1734], zoom_start=12)

folium.GeoJson(gdf).add_to(barcelona_map)


barcelona_map.save(r"C:\Users\nabal\Downloads\barcelona_districts.html")
