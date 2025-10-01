def main():
    print("Please, type in a message")
    message = input()
    dictionary = {} #empty dictionary
    c_count(message, dictionary)    #function where we'll use message and the dictionary
def c_count(m, d):  # defining said function
    for keys in m:  # for every element in the message...
        d.setdefault(keys, 0)   # add (to the dictionary) the characters individually, NOT repeating them, giving them a value of 0.
        d[keys] += 1    # add +1 to each character's value.     #(if the character is repeated, is not going to be added again, but it IS going to have its value added!!!)
    print(d)
    print(len(m))
    
main()