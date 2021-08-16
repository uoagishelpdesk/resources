# empty folium map for testing with portfolio stuff

import folium

m = folium.Map(location=(-36.85, 174.75), tiles='Stamen Terrain', control_scale=True, zoom_start=11)

m.save('map.html')