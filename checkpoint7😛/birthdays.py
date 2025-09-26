birthdays = { "Amaury": "June 1st",
             "Ariana": "August 11th",
             "Sara": "March 16th",
             "José": "May 19th"}
search = input("Please type a friend's name: ")
if search in birthdays:
        print(f"{search}'s birthday is on {birthdays[search]}")
else:
        print(f"I don't have {search}'s birthday info.")
        new_birthday = input("What's their birthday? ")
        birthdays[search] = new_birthday
        print("birthdays updated.")
        print(birthdays)