# names = []
# for i in range(3):
#     names.append(input("insert name: "))
# for name in sorted(names):
#     print(f"Hello, {name}.")

# name = input("What's your name? ")
# file = open("names.txt", "a") # w mean writing(from the beginning); a means append
# file.write(f"{name}\n") #write will work as a print for the file we're creating
# file.close() 

with open("names.txt", "a") as file:  # with  is a form of resuming file.close (there's no need to close it..?)
    file.write(f"{input("What's your name? ")}")

# with open("names.txt", "r") as file:     # r means reading
#     lines = file.readlines() #its turning into this: lines = ["Sen", "Hana", "Song", "Logan"]
# for line in sorted(lines):
#     print(f"Hello, {line.rstrip()}")