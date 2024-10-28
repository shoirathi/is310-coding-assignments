
import apikey
import os
import requests
import json

europeana_api_key = apikey.load("EUROPEANA_API_KEY")
os.environ['EUROPEANA_API_KEY'] = europeana_api_key

swampi_planet = "https://swapi.dev/api/planets/4/"
response_swampi_planet = requests.get(swampi_planet)
if response_swampi_planet.status_code == 200:
    swampi_planet_data = response_swampi_planet.json()
    print("swampi planet:", swampi_planet_data)
    search_term = swampi_planet_data['name']  # Use the planet's name as the search term
else:
    print("Failed to retrieve data from SWAPI.")

europeana_url = "https://www.europeana.eu/api/v2/search.json"
params = {
    "wskey": europeana_api_key,
    "query": search_term,
    "rows": 1
}
response_europeana = requests.get(europeana_url, params=params)
if response_europeana.status_code == 200:
    europeana_data = response_europeana.json()
    print("Europeana Data:", europeana_data)
    limited_europeana_data = europeana_data.get("items", [])[:1]
else:
    print("Failed to retrieve data from Europeana.")
filtered_data = {
    "Star Wars Planet Data": swampi_planet_data,
    "Europeana Data": limited_europeana_data
}
with open("starwars_hoth_europeana_data.json", "w") as json_file:
    json.dump(filtered_data, json_file, indent=4)
