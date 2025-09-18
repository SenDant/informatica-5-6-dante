# names = []
# for i in range(3):
#     names.append(input("insert name: "))
# for name in sorted(names):
#     print(f"Hello, {name}.")

name = input("What's your name? ")
file = open("names.txt", "a") # w mean writing(from the beginning); a means append
file.write(f"{name}\n") #write will work as a print for the file we're creating
file.close() 