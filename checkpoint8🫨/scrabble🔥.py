import random
import string
def main():
    alphabet = {
        "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
        "D": 2, "G": 2,
        "B": 3, "C": 3, "M": 3, "P": 3,
        "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
        "K": 5,
        "J": 8, "X": 8,
        "Q": 10, "Z": 10}
    user_letters = []
    i = 0
    while i < 13:   
        i += 1
        num = random.choice(string.ascii_uppercase)
        user_letters.append(num)
    print(user_letters)

    user_answer = input("Please, enter a word: ").upper()
    n = 0
    while n < len(user_answer):
        if user_answer[n] in user_letters:
            print(user_answer[n])
            n += 1
        else:
            print("nope")
            n += 1
        
    with open("scrabble_words.txt", "r") as file:
        lines = file.readlines()
        dictwords.append(line.replace"\n", ""))
main()