#------------------------------------------------- CREATING A DICTIONARY AND GETTING ITS CONTENT AND KEYS
capitals = {    # this is a dictionary.
    "Mexico": "Mexico City",
    "Canada": "Ottawa",
    "Brazil": "Brasilia"
    # (key) : (value)
}

capitals["Italy"] = "Rome"  # to add a new key and value to the dictionary.
del capitals["Brazil"] # deletes a key and its value, duh :p
#capitals.pop("Canada") # no difference from deleting.
capitals.clear() # to empty the dictionary.
print(capitals)
#print(capitals["Canada"]) 

#------------------------------------------------- GETTING THE VALUE OF A DICTIONARY'S KEY WITH A FOR LOOP
# houses = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }
# print(houses)

# for characters in houses:
#     print(f"{characters}'s house is {houses[characters]}.") # print the key, then the values but with the parameter of each key, so only each key's value

#------------------------------------------------- USING MATRIX TO GET +2 ELEMENTS
student_info = [{"Name": "Hermione", "House": "Gryffindor", "Patronus": "Otter"},         #each element of the list is a dictionary :O
          {"Name": "Harry", "House": "Gryffindor", "Patronus": "Stag"},
          {"Name": "Ron", "House": "Gryffindor", "Patronus": "Jack Russell Terrier"},
          {"Name": "Draco", "House": "Slytherin", "Patronus": None}
          ]
for student in student_info:
    print(f"{student["Name"]}'s house is {student["House"]} and their favorite Patronus is: {student["Patronus"]}") #checking through every element(dictionary) and using the
                                                                                                                    #key we want as a paremeter to get said key's value.