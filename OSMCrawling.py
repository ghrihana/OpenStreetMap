import requests
# Defining Overpass API query

query = """[out:json];area["name"="San Francisco"]->.searchArea;(  node["amenity"="restaurant"](area.searchArea); 

 way["amenity"="restaurant"](area.searchArea);  

 relation["amenity"="restaurant"](area.searchArea););

 out body;"""

 # Send the query to the Overpass API

 

response = requests.get("https://overpass-api.de/api/interpreter?data=" + query)

data = response.json()

print(data)
