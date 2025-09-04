def main():
    mess = input("Type a message: ").lower() #Ask user for input and store it in a variable called mess
    encode_message(mess) # execute a function where we'll use the mess variable

def encode_message(m): # the creation of said function
    alphabet = "abcdefghijklmnopqrstuvwxyz" #variable with the alphabet
    cypher = "zyxwvutsrqponmlkjihgfedcba" #variable with the cypher alphabet
    new_mess = "" # new variable that will have the encrypted message
    num = 0 # counter variable
    while num < len(m): # loop function that will work until the number of characters in the message hits the limit.
        num + 1 # counter is increasing
        chara = m[num] #new variable that will store every character in  the message with their position individually and progressively? i don't really understand this
        if chara in alphabet: #if the characters in the message exist in the alphabet, actions'll be performed.
            cypher_index = alphabet.find(chara) # new variable that'll find the characters in the alphabet stored in the chara variable
            new_mess += cypher[cypher_index] # the new message variable will concatenate(?) with the cypher letters; replacing every character of the alphabet in the message
                                             # with the characters in the cypher alphabet.
        else: #if there are characters that don't exist in the alphabet, actions'll be performed.
            new_mess += chara #the character will not be replaced.
        num += 1 #counter increases again so it keeps up with the characters in the if function..?
    print(f"Encrypthed message: {new_mess}") #print our new message with its characters already replaced.
    
main()
