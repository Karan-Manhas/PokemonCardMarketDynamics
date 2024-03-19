import requests as rq
import pandas as pd

# Make a request to the PokeAPI
response = rq.get("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0")
print(response.status_code)

# Extracting the list of Pokémon results from the JSON response
pokemon_results = response.json()["results"]

# Convert JSON to DataFrame
df = pd.DataFrame(pokemon_results)

# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Display entire DataFrame
print(df)
