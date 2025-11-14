import requests
API_KEY = "3HFBKUB6IZHM"

user = input("Where do you wish to know the local hour?")
timezones = requests.get(f"http://api.timezonedb.com/v2.1/convert-time-zone{API_KEY}")
print(timezones.json())
