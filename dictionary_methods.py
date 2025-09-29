dictionary = {
    "color": "black",
    "age": 18,
}
# values ᓚᘏᗢ!
print(dictionary.values())
for v in dictionary.values(): # .values returns a list with all the values ♪(^∇^*)
    print(v)
print("------------------")
# keys ᓚᘏᗢ!
print(dictionary.keys())
for k in dictionary.keys():
    print(k)
print("------------------")
# items ᓚᘏᗢ!
print(dictionary.items())
for i in dictionary.items():
    print(i)
print("------------------")
# print key and value using methods ᓚᘏᗢ! ???
#to do
print("------------------")
# Get ᓚᘏᗢ!
picnic_items = {"apples": 5, "cups": 2}
print(f"I'm bringing {picnic_items.get("cups",)} cups.") #it's going to get the value to specified key.
print(f"I'm bringing {picnic_items.get("eggs", 9)} eggs.") #there are no eggs, so it's gonna print None. 
                                                           #but we can put a number instead (, 9), so it print 9 if and only if there are none.
# Setting default values
pet_info = {
    "name": "Rayito",
    "age": "4"
}
pet_info.setdefault("color", "brown") # like append. ( same as: pet_info[color] = "brown" )
print(pet_info)