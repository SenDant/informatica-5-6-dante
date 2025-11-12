import requests
import json
def main():
    universities = {    #now im just missing the api to actually work...
        "Tecnológico de Monterrey": {"MAJORS" : 43, "SEMESTER COST": "$6,750USD", "CAMPUS": "1,112km", "URL": requests.get("http://www.")},
        "UACJ": {"MAJORS" : 100, "SEMESTER COST": "$137USD", "CAMPUS": "311km", "URL": requests.get(""+ answer)},
        "BYU Pathway": {"MAJORS" : 7, "SEMESTER COST": "$325USD", "CAMPUS": "1,607km", "URL": requests.get(""+ answer)},
        "Eastern Arizona": {"MAJORS" : 60, "SEMESTER COST": "$3,870USD", "CAMPUS": "428km", "URL": requests.get(""+ answer)},
        "Tecmilenio": {"MAJORS" : 43, "SEMESTER COST": "$3,200USD", "CAMPUS": "1,133km", "URL": requests.get(""+ answer)},}
    info(universities)

def info(unis):
    while True:
        try:
            print("Which university are you interested in?")
            answer = input("")
            print("-"*30)
            data = unis[answer]
            print(f"""The {answer} offers {data["MAJORS"]} majors, and has an average semester cost of {data["SEMESTER COST"]}.
The closest campus to your location is {data["CAMPUS"]} close to you.
Visit the official website at {data["URL"]}""")
            print("-"*30)
        except (KeyError, UnboundLocalError):
            print("That is NOT an university.")
main()