def main():
    #----EASY LEVEL----#
    list_length = int(input("List length: "))
    number_list = []
    for i in range(list_length):
        list_element = int(input("Enter an element: "))
        number_list.append(list_element)
    print(number_list)

    #---MEDIUM LEVEL---# I can't unu
    # print("------------------------------------")
    # print("Option 1: Enter a list.")
    # print("Option 2: Read numbers from a file.")
    # decision = int(input("Please, choose your option: "))
    # if decision <1 or decision >2:
    #     print("That is not an option.")
    # if decision == 1:
    #      serie = input("Please, enter a series of number sepparated by commas: ")
    # list_serie = list(serie)
    # write_numbers(list_serie)
   #read_numbers(list_serie)
   #find_largest(list_serie)

# def write_numbers(userlist):
#     file = open("largest.txt", "a")
#     for n in userlist:
#         file.write(n)
#     file.close

#def read_numbers():


#def find_largest():

main()