import requests
import json
song = input("what song r u looking for? ")
response = requests.get("https://itunes.apple.com/search?entity=song&limit=20&term="+ song) # get is to solicitar que nos de una response de ESE website.
# print(json.dumps(response.json(), indent=2))

search = response.json()
for result in search["results"]:
    print(result["trackName"], result["artistName"])

city = input("where do u live? ")
respons = requests.get("http://goweather.xyz/weather/"+ city)
print(respons.json())