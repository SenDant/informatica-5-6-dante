import requests
def main():
    API_KEY = "27be317712d2e0375eddb213e8dc4cf2fbbbb05662302b9b819757b6f9cb4e8b"
    try:
        wanted = float(input("How many bitcoins do u want to buy? "))
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey="+ API_KEY)
        bitcoin_price = float(response.json()["data"]["priceUsd"])
        total = round(wanted * bitcoin_price,2)
        print(f"You'll total will be ${total:,.2f}USD")
    except KeyError:
        print("Invalid input.")

main()