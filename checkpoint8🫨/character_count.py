def main():
    print("Please, type in a message")
    message = input()
    print("-------------------------")
    dictionary = {} #empty dictionary
    c_count(message, dictionary)    #function where we'll use message and the dictionary
def c_count(m, d):  # defining said function
    for keys in m:  # for every element in the message...
        d.setdefault(keys, 0)   # add (to the dictionary) the characters individually, NOT repeating them, giving them a value of 0.
        d[keys] += 1    # add +1 to each character's value.     #(if the character is repeated, is not going to be added again, but it IS going to have its value added!!!)
    print(d)
    print(f"the size of you message is of: {len(m)}.") # or print(sum(dictionary.values()))
    # Alternative 1 PRINT OUT THE MOST REPEATED NUMBER!
    values_list = list(d.values())
    largest_number_index = values_list.index(max(values_list))
    most_repeated = list(d.keys())[largest_number_index]
    print(f"the most repeated letter is: '{most_repeated}', repeated {d[most_repeated]} times.")
    # Alternative 2 PRINT OUT THE MOST REPEATED NUMBER!
    largest_number = max(d, key= d.get)
    print(f"the most repeated letter is: '{largest_number}', repeated {d[largest_number]} times.")
main()