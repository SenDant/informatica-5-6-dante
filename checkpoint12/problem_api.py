import requests
def main():
    API_KEY = "12MTRNXM5HQ6"
    while True:
        try:
            print("-"*55)
            answer = input("""        Type 1 to see the timezones list,
when you're ready, type 2 to type the desired timezone:
""")
            print("-"*55)
#-/---------------------------------------------------------------------------------------------------------------------------------------/-#
            if answer == "2":
                timezone = input("""Type the timezone you want to see the hour. Example: 'America/Mexico_City'
                              """)
                info_of_timezones = requests.get(f"http://api.timezonedb.com/v2.1/get-time-zone?key={API_KEY}&format=json&by=zone&zone={timezone}").json()
                if timezone == info_of_timezones["zoneName"]:
                    print(f"the timezone of {timezone} is: {info_of_timezones["formatted"][11:19]}")
                    break
                else:
                    print("The timezone does not exist or was written incorrectly.")
#-/---------------------------------------------------------------------------------------------------------------------------------------/-#
            elif answer == "1":
                print("""                   ---CONTINENTS---
Asia, America, Africa, Pacific, Europe
Antarctica, Australia, Atlantic, Indian, Arctic""")
                continent = input("Please, type the desired continent: ")
                info_of_continents = requests.get(f"http://api.timezonedb.com/v2.1/list-time-zone?key={API_KEY}&format=json&zoneName=*{continent}*").json()
                for all_zones in info_of_continents["zones"]:
                    zone = all_zones["zoneName"][:len(continent)]
                    if zone == continent:
                        print(all_zones["zoneName"])
            else:
                print("Invalid input.")
#-/---------------------------------------------------------------------------------------------------------------------------------------/-#
        except (KeyError, TypeError, UnboundLocalError, ValueError):
            print("An Unexpected Error Happened")
main()
